You can solve this problem by using the built-in function `max` with a custom key function that calculates the sum of elements in a list. Here is the Python solution:
```
def max_sum_list(list_of_lists):
    return max(list_of_lists, key=sum)
```
This function works by iterating over the list of lists and selecting the one with the highest sum of elements. The `key` argument of the `max` function is a function that takes a list as input and returns a value that will be used for comparison. In this case, the `key` function is `sum`, which calculates the sum of elements in a list. The `max` function then returns the list with the highest sum of elements. 

For example, if you call `max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])`, the function will return `[10, 11, 12]`, which is the list with the highest sum of elements. 

The unit test `assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]` ensures that the function works correctly.  It checks that the function returns the list `[10, 11, 12]` when given the input `[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]`. If the function works correctly, this test will pass.  If the function does not work correctly, this test will fail, indicating that the function needs to be fixed.  This is an important part of software testing, as it helps to ensure that the function works as expected.  Without unit tests, it can be difficult to determine whether a function is working correctly, especially in complex situations.  Unit tests provide a way to verify that a function is working correctly, which can help to catch errors and improve the overall quality of the software.  In this case, the unit test ensures that the `max_sum_list` function correctly returns the list with the highest sum of elements.  If the function does not work correctly, the unit test will fail, indicating that the function needs to be fixed.  This helps to ensure that the function works correctly and provides a way to verify that it is working as expected.  This is an important part of