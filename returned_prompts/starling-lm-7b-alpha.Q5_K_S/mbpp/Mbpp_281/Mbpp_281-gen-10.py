"""
def all_unique(L):
    """ Return True if all elements in the list L are unique, else False. """
    return len(L) == len(set(L))

def test_all_unique():
    assert all_unique([1,2,3]) == True
    assert all_unique([1,2,2]) == False
    assert all_unique([1,2,3,4,5,6]) == True
    print("All tests passed.")

test_all_unique()
"""

def all_unique(L):
    """ Return True if all elements in the list L are unique, else False. """
    if len(L) == len(set(L)):
        return True
    else:
        return False

def test_all_unique():
    assert all_unique([1,2,3]) == True
    assert all_unique([1,2,2]) == False
    assert all_unique([1,2,3,4,5,6]) == True
    print("All tests passed.")

test_all_unique()

```
    
This function will return True if all elements in the list are unique, and False otherwise. It does so by comparing the length of the list to the length of its set, which automatically removes all duplicate elements.

In this code, the function `all_unique()` takes in a list `L` as an argument. It first checks if the length of the list is equal to the length of the set of the list. If they are equal, it means that all elements in the list are unique, and it returns True. Otherwise, it returns False.

The `test_all_unique()` function is used to test the `all_unique()` function. It calls `all_unique()` with a few test cases and asserts that the expected output matches the actual output. If all tests pass, it prints "All tests passed.".

You can run this code to test the `all_unique()` function and ensure that it correctly determines if the elements in a list are unique or not.

```python
def all_unique(L):
    """ Return True if all elements in the list L are unique, else False. """
    if len(L) == len(