import numpy as np


def float_range(*args):
    """Given a start, end and interval, provides a list of floats"""

    numargs = len(args)
    if numargs == 0:
        raise TypeError("you need to write at lesae a value")
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(
            f"Inclusive range was expected at most 3 arguments, got {numargs}")
    i = start
    while i < stop:
        yield i
        i += step


if __name__ == "__main__":
    range = float_range(6, 1, -1)
    print(next(iter(range)))
    print(next(iter(range)))
    print(next(iter(range)))
    print(next(iter(range)))
