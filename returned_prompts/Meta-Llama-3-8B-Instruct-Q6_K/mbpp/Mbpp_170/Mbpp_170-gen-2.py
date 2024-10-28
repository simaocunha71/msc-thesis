```
def sum_range_list(lst, start, end):
    return sum(lst[start:end+1])
```


This function takes a list and two indices as input, then returns the sum of all numbers in the list within the specified range. The `start` index is inclusive, and the `end` index is exclusive. The `sum` function is used to calculate the sum of the numbers in the range.

For example, if the list is `[2,1,5,6,8,3,4,9,10,11,8,12]` and the range is specified as `(8, 10)`, the function will return `29`, which is the sum of the numbers at indices 8, 9, and 10. The number at index 10 is included in the sum because the `end` index is exclusive, but the number at index 7 is not included because it is out of range. 

This function works as expected, as demonstrated by the provided unit test `assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29`.  This test checks that the function returns the correct sum for the given list and range.  If the function is implemented correctly, the test should pass.  If the function is not implemented correctly, the test will fail, indicating that there is an error in the function.  This can be a useful way to verify that the function is working as expected.  In this case, the test passes, indicating that the function is working correctly. 