"""This module contains algorithms for generating the wall layout."""

from typing import List, Dict

from wall_builder.row_layout import row_layouts_dp
from wall_builder.neighbor import build_neighbors, no_common_edge

from wall_builder.utils.profiler import profile


def num_wall_layouts(
    brick_set: set, wall_length: int, wall_height: int, predicate=no_common_edge
) -> int:
    """Return the number of all possible wall layouts given a brick set, wall dimensions and
    given eligibility predicate of neighboring rows.

    Assumptions:
        - there're unlimited supply of bricks of each size
        - only use bricks horizontally

    The algorithm is broken down into three steps:
        1. Find all possible row layouts using Dynamic Programming (see :py:func:`~wall_builder.row_layout.row_layouts_dp`)
        2. Find eligible neighbors for each row layout according to the given predicate  (see :py:func:`~wall_builder.neighbor.build_neighbors`)
        3. Find the number of all possible wall layouts using Dynamic Programming  (see :py:func:`~wall_builder.wall_layout.num_wall_layouts_helper`)

    Args:
        brick_set (set): available bricks; each element is the length of a brick
        wall_length (int): length of the wall
        wall_height (int): height of the wall
        predicate (function): a function that takes in two row layouts' index and other keyword arguments,
          and returns True if they are eligible neighbors

    Returns:
        int: the number of all possible wall layouts
    """
    # Step 1: find all possible row layouts
    row_layouts = row_layouts_dp(brick_set, wall_length)

    # Step 2: find eligible neighbors for each row layout
    neighbors = build_neighbors(row_layouts, predicate=predicate)

    # Step 3: find the number of all possible wall layouts
    return num_wall_layouts_helper(neighbors, wall_height)


def num_wall_layouts_helper(neighbors: Dict[int, List[int]], wall_height: int) -> int:
    """Return the number of all possible wall layouts using Dynamic Programming.

    The time complexity is O(NK'), where N is the wall height and K' is the average number of possible neighbors, which is proportional to the number of row layouts, K.
    The memory complexity is O(K"), where K" is the length of ``neighbors``, which is proprotional to the number of row layouts, K.

    Args:
        neighbors (Dict[int, List[int]]): a dictionary of row layouts (index) mapped to their eligible neighbors (index).
            Eligibility is defined as the neighboring two rows don't share an edge.
        wall_height (int): height of the wall

    Returns:
        int: the number of all possible wall layouts
    """
    # Step 1: initialize the DP cache;
    # normally a DP table would be used, but in this case we only need the states for the current and previous layouts
    # use a dictionary to save space, esp. when not all row_layouts are in neighbors dictionary
    prev_dp_cache = {item: 1 for item in neighbors}

    # Step 2: fill in the DP cache
    for _ in range(1, wall_height):
        curr_dp_cache = {item: 0 for item in neighbors}
        for j, n_list in neighbors.items():
            for neighbor in n_list:
                curr_dp_cache[j] += prev_dp_cache[neighbor]
        prev_dp_cache = curr_dp_cache

    # Step 3: return the sum of the last current DP cache
    return sum(curr_dp_cache.values())


__all__ = ["num_wall_layouts", "num_wall_layouts_helper"]

if __name__ == "__main__":
    assert num_wall_layouts(set([2, 3]), 30, 12) == 16879522589829476
