```
def combinations_colors(lst, n):
    return [tuple(x) for x in itertools.product(lst, repeat=n)]
```
The function uses the itertools.product function to generate all combinations of the elements in the list with the specified length. The result is a list of tuples, where each tuple is a combination of the elements from the list.

The unit test `assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]` checks that the function correctly generates all combinations of the elements in the list with length 1.

Note: The itertools module is a part of Python's standard library. It provides functions for working with iterators, such as the product function used in this solution. If you're not familiar with the itertools module, I'd be happy to explain more about it!