"""
def nth_nums(lst,n):
    return [i**n for i in lst]
"""

def nth_nums(lst,n):
    return [pow(i,n) for i in lst]

from hypothesis import given, settings, assume
from hypothesis.strategies import lists, integers
@given(lists(integers()), integers())
@settings(max_examples=10000)
def test_nth_nums(lst,n):
    assert nth_nums(lst,n) == [i**n for i in lst]

test_nth_nums()

"""
Explanation:
This program defines a function called nth_nums that takes in a list and an integer n.
The function uses a list comprehension to create a new list, where each element is the n-th power of the corresponding element in the input list.
The function then returns this new list.
The program also includes a test using the Hypothesis testing library to verify that the function works correctly.
"""

```python

```