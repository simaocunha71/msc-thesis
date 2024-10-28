```
def split_Arr(arr,n):
    if n > len(arr):
        return arr
    else:
        return arr[n:]+arr[:n]
```


This function takes a list and an integer as input. It then checks if the integer is greater than the length of the list. If it is, it simply returns the original list. If the integer is not greater than the length of the list, it splits the list at the nth element using list slicing and then concatenates the two parts in reverse order. The first part of the list (from the start to the nth element) is added to the end of the second part (from the nth element to the end). The result is then returned. The unit test `assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]` ensures that the function works correctly.  It checks that the function splits the list at the 2nd element and adds the first part to the end, resulting in the list [5,6,52,36,12,10].  If the function does not work correctly, the unit test will raise an AssertionError.  This helps to ensure that the function is working as expected.  The unit test can be run with the `unittest` module in Python.  For example, you can create a test function like this:

```
import unittest

def test_split_Arr():
    assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
    return 'Test passed'

print(test_split_Arr())
```

If the function is working correctly, this will print `'Test passed'`.  If the function is not working correctly, this will raise an AssertionError.  You can add more unit tests to ensure that the function works correctly for different inputs.  For example, you can add a test to check that the function works when the input list is empty:

```
assert split_Arr([],2) == []
```


This ensures that the function returns an empty list when given an empty list as input.  You can add more unit tests as needed to ensure that the function works correctly for different inputs.  The unit tests can be run with the `unittest` module in Python.  For example, you can create a test class like this:

```
import unittest

class TestSplitArr(unittest.TestCase):
   