"""
Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
"""
from typing import Callable, Any, Optional, List, Dict
from functools import wraps
import copy
from itertools import islice, chain

def flatten(nested_list: list) -> list:
    return [x for l in nested_list for x in l]

def get_index_of_array_element(arr_elt: Any, *, arr: List[Any]) -> int:
    def innerfunc(*, **):
        if type(arr) is not list and not hasattr(arr, '__iter__'):
            raise TypeError("Expected an array but got {}.".format(type(arr)))
        for i in range(0, len(arr)):
            try:
                return arr[i] == arr_elt and i or -1
            except ValueError as e:
                pass
    return innerfunc  # pyright: add trailer

def sequential_search(arr: List[Any], *args, **kwargs) -> Any:
    def inner_function(*args):
        if callable(arr) == False:
            raise TypeError("Expecting a mutable collection as input but got {}".format(type(arr)))
        #  Create the output
        output = () in args and getattr((copy.deepcopy(args[0]), "__iter__")(), type(0))()
        def inner_func(*args) -> Any:
            def decorated_inner_fun(*args):
                if callable(arr) == False:
                    raise TypeError("Expecting a mutable collection as input but got {}".format(type(arr)))
                try:
                    output = arr[output]
                except ValueError as e:
                    pass
            return decorated_inner_fun  # pyright: add trailer
        if type(arr) is not list and callable(arr):
            arr = [i for i in chain(*args)]
        else:
            arr = flatten(islice(args, 1))
        return inner_func(*args)
    return inner_function()   # pyright: add trailer
