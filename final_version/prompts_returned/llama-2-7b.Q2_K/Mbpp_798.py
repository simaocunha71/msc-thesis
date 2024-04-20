"""
Write a python function to find the sum of an array.
assert _sum([1, 2, 3]) == 6
"""
from typing import Callable, Any, Union
import numpy as np


def _run_and_print(func: Callable, *args) -> None:
    if args and isinstance(args[-1], (list, tuple)):
        # Include the input array to the output of the function.
        res = func(*args)
    else:
        res = func(*tuple(args))
    print("Result:", end="\t")
    if type(res) is list:
        print("\t".join([str(x) for x in res]))
    else:
        print(type(res).__name__ + " (size: " + str(len(res)) + ")")


def _sum(*args: Any, **kwargs: Union[str, int]) -> float:
    if isinstance(args[-1], (list, tuple)):
        assert kwargs.get('verbose'), "Verbosity is disabled by default."
        return np.array([float(_) for _ in args]).sum()
    else:
        # The input is already a numpy array; we don't need to make it one first.
        return float(np.array(_) if _ else [])  # noqa: WPS21,WPS395
