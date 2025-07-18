def give_bmi(h: list[int | float], w: list[int | float]) -> list[int | float]:
    '''
        returns a list of bmi values
        bmi = w / (h * h)
    '''
    try:
        assert len(h) == len(w), "AssertionError, lists are not the same size"
        assert type(h) is type(w), "AssertionError, wrong types"
        assert 0 not in h and 0.0 not in h, "AssertionError, division by zero"
    except AssertionError as err:
        print(err)

    return [w / (h * h) for h, w in zip(h, w)]


def apply_limit(lst: list[int | float], limit: int) -> list[bool]:
    '''Returns true for each elem in lst if elem is above limit'''
    return [float(e) > float(limit) for e in lst]
