```
def square_nums(nums):
    return [num ** 2 for num in nums]
```
This function uses a list comprehension to square each number in the input list. The `**` operator is used to square a number, and the result is added to the list. The resulting list is then returned.

The unit test `assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` ensures that the function works correctly. It checks that the function returns the expected result when given the input list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. If the function returns the correct result, the unit test passes; otherwise, it fails.