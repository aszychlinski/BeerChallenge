def test_name(test_data):
    failures = []
    for beer in test_data:
        name = beer['name']
        if (type(name) != str) or (len(name) == 0):
            failures.append(beer['id'])

    assert not failures, 'Beers with these IDs do not meet the validation criteria for name'
