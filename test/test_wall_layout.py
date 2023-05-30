"""This module tests the wall layout algorithms."""

import pytest
from wall_builder.wall_layout import num_wall_layouts


@pytest.mark.parametrize(
    "brick_set, wall_length, wall_height, expected",
    [
        (set([2, 3]), 5, 2, 2),
        (set([2, 3]), 6, 2, 2),
        (set([2, 3]), 5, 3, 2),
        (set([2, 3]), 6, 3, 2),
        (set([1, 2, 3]), 6, 3, 176),
        (set([1, 2, 4]), 6, 5, 1336),
        (set([2, 3]), 30, 12, 16879522589829476),
    ],
)
def test_num_wall_layouts(brick_set, wall_length, wall_height, expected):
    assert num_wall_layouts(brick_set, wall_length, wall_height) == expected
