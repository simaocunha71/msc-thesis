"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum([1,2,3]) == 4
"""
from typing import Any, Dict, List, Optional, Tuple, Type, Union # noqa: E501

import ast
import copy
# from itertools import chain
from pyright_utils.ast_parsing.visitors.function_body import body_tokens_for_node_ast
from pytest import fixture
from pyright_utils.types import get_subtype # noqa: E501

from .utils import (
    assert_python,
    assert_types,
    assert_validates,
    create_context,
)
from ...ast import (
    AST_NODE_FUNCTION,
    AST_NODE_VARIABLE,
    AST_TYPE_BOOLEAN,
    AST_NODE_TUPLE,
    AST_NODE_LIST,
)
from ...types import (
    ANNOTATIONS,
    FUNCTION,
    LARGEST_VALUE_FUNCTION,
    MAXIMUM_LARGEST_INPUT_SHORTENED,
    MAXIMUM_SMALLEST_INPUT_SHORTENED,
)
from ...types.primitives import BOOLEAN
from typing import Any, Dict, List, Optional, Tuple, Type, Union
__all__ = [
    "big_sum",
]

context = create_context()
context_dict = copy(context)


def big_sum(*values: Any) -> int:
    """big_sum function."""
    assert len(values) > 0, "len of values should be greater than zero."

    assert isinstance(values[0], AST_TYPE_BOOLEAN), "assert that all the values are boolean."
    if not isinstance(values[0], AST_TYPE_BOOLEAN):
        raise TypeError("The types of input values should be boolean.")

    assert len(values) > 1, "len of values should be greater than one. So far, I've found the biggest, but still no smallest."

    for v in range(1, len(values)):
        if not isinstance(values[v], AST_TYPE_BOOLE