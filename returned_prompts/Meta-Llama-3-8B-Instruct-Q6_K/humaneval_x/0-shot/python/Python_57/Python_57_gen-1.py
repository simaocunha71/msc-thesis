You can solve this problem by comparing each element in the list with the previous one. If all elements are monotonically increasing or decreasing, the function should return True. Otherwise, it should return False.

Here is the Python code for the problem:

```
def monotonic(l: list):
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    return increasing or decreasing
```

This function uses the built-in Python functions `all()` and `range()` to iterate over the list and compare each element with the previous one. The `all()` function returns True if all elements in the given iterable are True. If at least one element is False, it returns False. The `range()` function generates a sequence of numbers from 0 to the length of the list minus one.

The function `monotonic()` returns True if the list is either monotonically increasing (`increasing` is True) or decreasing (`decreasing` is True). Otherwise, it returns False. This solution works for lists of any size and with any type of elements. It also works for lists that are not sorted, as long as they are monotonically increasing or decreasing.

The unit tests provided in the problem ensure that the function works correctly for different types of lists. For example, the test `>>> monotonic([1, 2, 4, 20])` checks that the function returns True for a list that is monotonically increasing. The test `>>> monotonic([1, 20, 4, 10])` checks that the function returns False for a list that is not monotonically increasing or decreasing. The test `>>> monotonic([4, 1, 0, -10])` checks that the function returns True for a list that is monotonically decreasing. These tests ensure that the function works correctly for different types of lists.