def test_abv(test_data):
    failures = []
    for beer in test_data:
        abv = beer['abv']
        if (type(abv) != float) or (abv <= 4):
            failures.append(beer['id'])

    assert not failures, 'Beers with these IDs do not meet the validation criteria for ABV'

# Checking for null or empty string would be redundant, as the type check for float already covers that.
# Also because the 'or' operator short-circuits, it prevents an exception caused by comparing 4 to a non-numeric type.
# Differentiation between int and float in the 'test_data' dict is implicitly reliant on this conversion table:
# https://docs.python.org/3/library/json.html#encoders-and-decoders
