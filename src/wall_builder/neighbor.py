"""This module contains algorithms for finding the eligible neighbors of each row layout."""

from typing import List, Dict, Callable
from collections import defaultdict
import numpy as np


def no_common_edge(
    i: int,
    j: int,
    cum_sums: Dict[int, List[int]],
) -> bool:
    """Return True if the layouts at indices i and j have a common edge.
    Cum_sum for each row layout is pre-calculated to avoid repeated calculations.
    If the cum_sum of two row layouts have a common element except for the last one, then the two layouts have a common edge.
    """

    # ignore the last element of each cum_sum because it is the total length of the row
    assert cum_sums[i][-1] == cum_sums[j][-1]
    return set(cum_sums[i][:-1]) & set(cum_sums[j][:-1]) == set()


def calc_cum_sums(row_layouts: List[List[int]]) -> Dict[int, List[int]]:
    """Helper function to calculate cumumative sum of length for each row layout."""
    cum_sums = [[] for _ in range(len(row_layouts))]
    for i, layout in enumerate(row_layouts):
        cum_sums[i] = np.cumsum(layout)
    return cum_sums


def build_neighbors(
    row_layouts: List[List[int]], predicate: Callable = no_common_edge
) -> Dict[int, List[int]]:
    """Return a dictionary mapping each layout's index to its eligible neighbors' index.
    
    The runtime complexity is O(K^2) where K is the number of row layouts.
    The memory complexity is O(K^2) where K is the number of row layouts.
    
    Args:
        row_layouts (List[List[int]]): a list of row layouts
        predicate (Callable, optional): the predicate for eligible neighboring rows. Defaults to no_common_edge.

    Returns:
        Dict[int, List[int]]: a dictionary mapping each layout's index to its eligible neighbors' index
    """

    cum_sums = calc_cum_sums(row_layouts)
    neighbors = defaultdict(list)
    for i in range(len(row_layouts) - 1):
        for j in range(i + 1, len(row_layouts)):
            if predicate(i, j, cum_sums=cum_sums):
                neighbors[i].append(j)
                neighbors[j].append(i)

    return neighbors


__all__ = ["build_neighbors", "no_common_edge", "calc_cum_sums"]
