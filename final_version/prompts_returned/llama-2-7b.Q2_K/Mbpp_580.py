"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""
import functools
from typing import Any, Dict, Optional, TypeVar, Generic, List, Set, Tuple
from typing_extensions import Probability, Sequence

F = TypeVar('F', bound=float)
T = TypeVar('T')


def extract_even(x: T, rnd: Probability) -> Dict[str, Any]:
    """Decorator to extract even elements from a nested tuple."""
    class ExtractorEven(Generic[F]):
        def __init__(self, rng=None):
            self.rng = rng if rnd is None else rng()  # type: ignore

        def __call__(self, even_tuple: F) -> Any:
            return {k: v for k, v in even_tuple.items()}
    return functools.partial(ExtractorEven, rng=rnd)
