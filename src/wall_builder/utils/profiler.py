"""This module contains a decorator to profile a function."""

import cProfile
from pstats import Stats, SortKey


def profile(func):
    """Decorator to profile a function. 
    The profile result will be printed out and saved as ``./prof/{func.__name__}.prof``.
    The saved stats can be viewed with snakeviz by running ``snakeviz ./prof/{func.__name__}.prof`` in the terminal.

    Args:
        func: the function to be profiled.
    """
    def wrapper(*args, **kwargs):
        with cProfile.Profile() as pr:
            result = func(*args, **kwargs)

        stats = Stats(pr).sort_stats(SortKey.TIME)
        stats.dump_stats(f"./prof/{func.__name__}.prof")
        stats.print_stats()
        return result

    return wrapper
