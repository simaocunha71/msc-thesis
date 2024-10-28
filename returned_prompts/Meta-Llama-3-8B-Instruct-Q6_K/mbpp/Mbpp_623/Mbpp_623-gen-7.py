```
def nth_nums(nums, n):
    return [num**n for num in nums]
```
This function uses a list comprehension to square each number in the input list. The `**` operator is used to raise each number to the power of `n`. The result is a new list containing the `n`-th power of each number in the input list.

For example, if the input list is `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` and `n` is `2`, the output will be `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`. This is because the square of each number in the input list is computed and the result is a new list containing these squared numbers. 

The unit test `assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` verifies that the function works correctly for the given input and `n`. 

This function is efficient because it uses a list comprehension, which is a built-in Python feature that can be used to create lists in a concise and efficient way. The time complexity of this function is O(n), where `n` is the length of the input list, because it needs to iterate over the input list once to compute the `n`-th power of each number. The space complexity is also O(n), because it needs to store the result in a new list that has the same length as the input list. 