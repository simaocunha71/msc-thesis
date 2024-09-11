"""
The function `remove_nested` takes a tuple as input and returns a new tuple with all the tuples removed.

Here is a step-by-step explanation of the solution:

- The function `remove_nested` takes a single parameter called `t` which is the input tuple.
- An empty list called `result` is created to store the elements that are not tuples.
- A while loop is used to iterate through the input tuple. The loop will continue until the entire tuple is traversed.
- Inside the loop, each element of the tuple is checked using the `isinstance` function to determine if it is a tuple or not.
    - If the element is not a tuple, it is added to the `result` list using the `append` method.
    - If the element is a tuple, the function `remove_nested` is recursively called on the tuple to remove any nested tuples. The result of this recursive call is appended to the `result` list.
- After the loop is finished, the `result` list is converted back to a tuple using the `tuple` function and returned as the final result.
- The `assert` statement is used to test the function with the given example `(1, 5, 7, (4, 6), 10)` and it should return `(1, 5, 7, 10)`.
"""

import sys

def remove_nested(t):
    result = []
    for i in t:
        if not isinstance(i, tuple):
            result.append(i)
        else:
            result.append(remove_nested(i))
    return tuple(result)

def test_remove_nested():
    assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
    assert remove_nested((1, (2, (3, 4)), 5)) == (1, 2, 3, 4, 5)
    assert remove_nested((1, 5, 7, (4, 6), 10, (11, (12, 13)), 14)) == (1, 5, 7, 