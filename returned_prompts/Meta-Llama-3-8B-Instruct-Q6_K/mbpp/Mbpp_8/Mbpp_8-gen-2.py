```
def square_nums(nums):
    return [num ** 2 for num in nums]
```
This function uses a list comprehension to create a new list where each element is the square of the corresponding element in the input list. For example, if the input list is `[1, 2, 3, 4, 5]`, the output list will be `[1, 4, 9, 16, 25]`. The `**` operator is used to calculate the square of a number. 

The unit test `assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` ensures that the function works correctly for the given input. 

This solution has a time complexity of O(n), where n is the number of elements in the input list, because it iterates over the input list once. The space complexity is also O(n), because it creates a new list with the same number of elements as the input list. 