```
def nth_nums(nums, n):
    return [num ** n for num in nums]
```


This function takes a list of numbers and an integer `n` as inputs, and returns a new list where each number in the input list is raised to the power `n`. The function uses a list comprehension to achieve this.

For example, if you call `nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)`, the function will return `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`, which are the squares of the numbers in the input list.