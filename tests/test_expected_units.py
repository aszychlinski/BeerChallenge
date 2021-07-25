EXPECTED_UNITS = {
    'volume': ('litres',),
    'boil_volume': ('litres',),
    'temp': ('celsius', 'fahrenheit'),
    'amount': ('grams', 'kilograms')
}


def test_expected_units(test_data):
    """Check if the value of all instances of 'unit' in the json falls within a predefined range of values.

    This test case will attempt to recursively walk the entire json.
    It passes the name of the parent node down the stack as it does so.
    Whenever it finds the key 'unit', it will check if its value is in a collection of acceptable values.
    Which values are acceptable is based on the name of the parent node.
    This is stored in the EXPECTED_UNITS map.
    When an unexpected unit is found, an Exception is raised to break out of the stack and signal a failure.
    Otherwise, if the walk function implicitly returns None, it is considered as a pass for that particular beer.
    You can verify this test case by running with the --source=cached argument and changing units in data.json.
    """

    def walk(map_: dict, parent: str) -> None:
        for item in map_:
            if type(map_[item]) == dict:
                walk(map_[item], item)
            if type(map_[item]) == list:
                for list_item in map_[item]:
                    if type(list_item) == dict:
                        walk(list_item, item)
            if item == 'unit' and type(map_[item]) == str:
                if map_[item] not in EXPECTED_UNITS[parent]:
                    raise ValueError

    failures = []
    for beer in test_data:
        try:
            walk(beer, '')  # empty string passed as "parent" to handle root element not having a parent
        except ValueError:
            failures.append(beer['id'])

    assert not failures, 'Beers with these IDs have at least one misspelled or otherwise unexpected unit'
