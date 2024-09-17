```
def nth_nums(nums, n):
    return [i**n for i in nums]
```
This function takes a list of numbers and an integer n as input, and returns a new list where each number is raised to the power of n. The unit test `assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` ensures that the function works correctly. The function uses a list comprehension to iterate over the input list, raising each number to the power of n using the `**` operator. The result is a new list containing the n-th powers of each number in the input list. For example, `nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)` would return `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`. 