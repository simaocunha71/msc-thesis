```
def square_nums(nums):
    return [num ** 2 for num in nums]
```


The problem asks to create a function that takes a list of numbers and returns a new list where each number is squared.

The unit test provided, `assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`, helps clarify the problem by showing the expected output for a given input.

The solution uses a list comprehension to create a new list where each element is the square of the corresponding element in the input list. The `**` operator is used to raise each number to the power of 2, effectively squaring it. The resulting list is then returned by the function.