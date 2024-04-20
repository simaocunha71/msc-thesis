"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union, overload

T = TypeVar('T', None, int)  # type: ignore[union-attr]
V = TypeVar('V')  # type: ignore[union-attr]

def is_product_even(
    even_func: Callable[[Dict[str, V]], List[Any]]
) -> Any:
    """Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])"""  # noqa: E501


def test_it() -> None:
    """Test it."""
    pass