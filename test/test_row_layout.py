"""This module tests the row_layout module"""

import pytest
from hypothesis import given, strategies as st

from wall_builder.row_layout import row_layouts, row_layouts_dp


@pytest.fixture(scope="module", params=[row_layouts, row_layouts_dp])
def row_layout_func(request):
    """Return the row_layout function to test."""
    return request.param


@pytest.mark.parametrize("brick_set, row_length", [
    (set([]), 0),
    (set([]), 1),
    (set([2]), 0),
    (set([2, 3]), 1),
    (set([2, 3]), 2),
    (set([2, 3]), 3),
    (set([2, 3]), 4),
    (set([2, 3]), 5),
    (set([2, 3]), 30),
    (set([2, 3, 31]), 30),
    ]
)
# @given(
#     brick_set=st.sets(st.integers(min_value=1, max_value=5)),
#     row_length=st.integers(min_value=0, max_value=30),
# )
def test_row_layouts(row_layout_func, brick_set, row_length):
    """Test row_layouts"""
    all_layouts = row_layout_func(brick_set, row_length)

    for layout in all_layouts:
        assert sum(layout) == row_length
        assert all(brick in brick_set for brick in layout)

    # check for duplicates
    assert len(set(map(tuple, all_layouts))) == len(all_layouts)
