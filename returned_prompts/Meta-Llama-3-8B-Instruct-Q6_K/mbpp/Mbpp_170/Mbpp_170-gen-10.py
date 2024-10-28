```
def sum_range_list(lst, start, end):
    return sum(lst[start:end+1])
```
This function takes a list `lst`, and two indices `start` and `end` as input. It returns the sum of the elements in the list from the `start` index to the `end` index (inclusive). The `end` index is inclusive, which means the element at that index is also included in the sum.

For example, if the list is `[2,1,5,6,8,3,4,9,10,11,8,12]`, and the start index is 8, and the end index is 10, the function will return the sum of the elements at indices 8, 9, and 10, which are 8, 9, and 11, respectively. The sum of these elements is `8 + 9 + 11 = 29`. This is confirmed by the unit test `assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29`. 