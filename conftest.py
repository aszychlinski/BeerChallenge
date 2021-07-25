from json import dumps, loads
from os.path import isfile

import pytest
from requests import get


def pytest_addoption(parser):
    parser.addoption('--source', action='store', default='online', help='"online" or "cached" (json)')


@pytest.fixture(scope='session')
def test_data(request):
    """Procure json with beers, which is then provided to individual test cases via dependency injection.

    scope='session' causes this to be prepared once per test suite launch, saving both runtime and bandwidth
    """

    option = request.config.getoption('--source')
    if option == 'cached':
        if not isfile('data.json'):
            raise FileNotFoundError('no cached data found')
        else:
            with open('data.json', encoding='utf-8', mode='r') as file:
                output = loads(file.read())

    else:
        response = get('https://api.punkapi.com/v2/beers?brewed_after=12_2015')
        if response.status_code == 200:
            output = response.json()
            with open('data.json', encoding='utf-8', mode='w') as file:
                file.write(dumps(output))
        else:
            raise RuntimeError('unexpected response')

    return output

