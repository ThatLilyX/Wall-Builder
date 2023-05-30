"""This module contains algorithms for laying out rows of bricks."""

from typing import Set, List
from wall_builder.utils.profiler import profile


def row_layouts(brick_set: Set[int], row_length: int) -> List[List[int]]:
    """Return a list of all possible row layouts for a given brick set and row length using recursion.
    This function is inefficient and only used to check the correctness of the Dynamic Programming solution.
    """

    if row_length == 0:
        return [[]]
    layouts = []
    for brick in brick_set:
        if brick > row_length:
            continue
        for layout in row_layouts(brick_set, row_length - brick):
            layouts.append([brick] + layout)
    return layouts


def row_layouts_dp(brick_set: Set[int], row_length: int) -> List[List[int]]:
    """Return a list of all possible row layouts for a given brick set and row length using Dynamic Programming.
    
    The runtime complexity is O(MNK) and the memory complexity is O(N^2K), 
    where M is the length of the brick set, N is the row length and K is the 
    average number of possible row layouts w.r.t. the row length.
    
    An upper bound of K is proportional to N!. As the worst case is to 
    have M = N, brick_set = {1, 2, ..., N} and row_length = N.

    Args:
        brick_set (Set[int]): available brick types; each element is the length of a brick
        row_length (int): length of the row, i.e. the length of the wall

    Returns:
        List[List[int]]: the list of all possible row layouts
    """

    layouts = [[] for _ in range(row_length + 1)]

    for brick in brick_set:
        if brick <= row_length:
            layouts[brick] = [[brick]]

    for length in range(1, row_length + 1):
        layouts.append([])
        for brick in brick_set:
            if brick > length:
                continue
            for layout in layouts[length - brick]:
                layouts[length].append([brick] + layout)

    return layouts[row_length]


__all__ = ["row_layouts", "row_layouts_dp"]

if __name__ == "__main__":
    assert (
        len(row_layouts_dp(set([2, 3]), 30))
        == 1897
        == len(row_layouts(set([2, 3]), 30))
    )
