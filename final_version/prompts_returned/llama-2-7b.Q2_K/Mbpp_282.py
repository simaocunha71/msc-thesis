"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""
from typing import Any, Callable, Dict, List, Optional, Set

# Third party libs
from collections import namedtuple
import numpy as np

_N_DIM = int(np.sqrt(len(set(_N_DIM))))


class _ND_Dim:
    """Stores dimension info."""
    def __init__(self, dim: int):
        self._dim = dim


# First party libs
from typing import List
from collections import namedtuple, MutableMapping

_N_DIM = list(_ND_Dim(0))

# noinspection PyArgumentList
def _sub_list(
    A: Optional[List] = None, B: Optional[List] = None,  # type: ignore
    out: Optional[List] = None, **kwargs : Any
) -> List:
    """Subtract two lists element-wise and return result."""
    if not all(isinstance(x, MutableMapping) for x in A):
        raise TypeError('A must be of type MutableDict!')

    if not all(isinstance(y, MutableMapping) for y in B):
        raise TypeError('B must be of type MutableDict!')

    _N_DIM = kwargs['dim'] if 'dim' in kwargs and kwargs['dim'] is not None else len(_N_DIM)
    dim : int = _N_DIM + 1,
    # type: ignore [index 0 is never used]
    dim2 : int = _N_DIM + 1,

    if out is None:
        out = [None] * (_N_DIM)
    else:
        assert isinstance(out, list), f'Out must be of type List!'

    for n in range(_N_DIM):
        out[n] = _out_getter(out[n])  # type: ignore [index 0 is never used]
    for d in range(dim, dim2):
        for n in range(d + 1):  # type: ignore [index 0 is never used]
            out[d] = _sub_list_elementwise(_sub_list(out[n],