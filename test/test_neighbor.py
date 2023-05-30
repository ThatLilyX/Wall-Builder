"""This module tests the neighbor module."""

import pytest

from wall_builder.row_layout import row_layouts_dp
from wall_builder.neighbor import build_neighbors, no_common_edge, calc_cum_sums


@pytest.fixture(
    scope="module",
    params=[(set([2, 3]), 5), (set([2, 3]), 6), (set([1, 2, 3]), 6), (set([2, 3]), 30)],
)
def row_layouts(request):
    return row_layouts_dp(*request.param)


@pytest.mark.parametrize(
    "cum_sums, i, j, expected",
    [
        ({0: [3, 6], 1: [2, 4, 6], 2: [1, 3, 6], 3: [1, 2, 3, 4, 5, 6]}, 0, 1, True),
        ({0: [3, 6], 1: [2, 4, 6], 2: [1, 3, 6], 3: [1, 2, 3, 4, 5, 6]}, 0, 2, False),
        ({0: [3, 6], 1: [2, 4, 6], 2: [1, 3, 6], 3: [1, 2, 3, 4, 5, 6]}, 0, 3, False),
        ({0: [3, 6], 1: [2, 4, 6], 2: [1, 3, 6], 3: [1, 2, 3, 4, 5, 6]}, 1, 2, True),
    ],
)
def test_no_common_edge(cum_sums, i, j, expected):
    """Test no_common_edge"""
    assert no_common_edge(i, j, cum_sums) == expected


def test_build_neighbors(row_layouts):
    """Test build_neighbors"""
    neighbors = build_neighbors(row_layouts, predicate=no_common_edge)
    cum_sums = calc_cum_sums(row_layouts)

    for i, n_list in neighbors.items():
        for j in n_list:
            assert no_common_edge(i, j, cum_sums=cum_sums)
