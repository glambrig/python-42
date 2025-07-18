import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
        Write a function that takes as parameters a 2D array,
        prints its shape, and returns a
        truncated version of the array based on the provided start
        and end arguments.
    '''

    try:
        # this?
        assert type(family) is list, "wrong types"
        # or this?
        assert type(family) is np.ndarray, "wrong types"

        assert type(start) is int and type(end) is int, "wrong types"
    except AssertionError as err:
        print(f"AssertionError, {err}")

