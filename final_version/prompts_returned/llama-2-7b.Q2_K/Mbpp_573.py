"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""
from typing import Any
import functools

def get_list_of_positive_numbers(n: int):
    """Returns a copy of the input list with all entries being positive integers."""
    return [i for i in range(1, n + 1)]

def unique_product(*args: Any) -> Any:
    def inner(self, *args: Any) -> Any:
        if not args:
            raise Exception("Expecting at least one number!")
        elif not type(args[0]) is int or type(args[0]) is float:
            return 1 # we're assuming that the inputs are all integers now.
        else:
            product = 1
            for i in args:
                if i == 0 and len(str(i)) > 1:
                    raise Exception("Zero must be a single character!") # 2x
                elif i == 0 or type(i) is int:
                    continue # we're not interested on zeroes so that's easy.
                elif i == None and self.__get_unique_positive_numbers__ > 1:
                    raise Exception("No negative numbers allowed!") # 3x (for-loop)
                elif type(i) is float or isinstance(i, complex):
                    pass # we'll handle this later.
                else:
                    try:
                        product *= self.__get_unique_positive_numbers__[0]
                    except IndexError as e:
                        raise Exception("Could not add the {} to the product! {}".format(e, str(args))) # 4x
            return product
    return functools.reduce(inner, args)
