import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
        Write a function that takes as parameters a 2D array,
        prints its shape, and returns a
        truncated version of the array based on the provided start
        and end arguments.
    '''

    arr = np.array(0)
    try:
        assert type(family) is list, "wrong types"
        arr = np.array(family)
        assert type(arr) is np.ndarray, "wrong types"
        assert arr.ndim == 2, "wrong number of array dimensions"
        assert type(start) is int and type(end) is int, "wrong types"
    except AssertionError as err:
        print(f"AssertionError, {err}")
        return
    except Exception:
        print("critical error")
        return

    print(f"My shape is ({len(arr)}, {arr.ndim})")
    newArr = arr[start:end]
    print(f"My new shape is ({len(newArr)}, {newArr.ndim})")
    return arr[start:end]
