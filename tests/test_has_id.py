def test_has_id(test_data):
    """Because the other tests identify failed beers by id, it is important to verify that all beers do have one."""
    for beer in test_data:
        if (type(beer.get('id')) != int) or (beer.get('id') < 1):
            assert False, 'At least one beer has an incorrect ID'
