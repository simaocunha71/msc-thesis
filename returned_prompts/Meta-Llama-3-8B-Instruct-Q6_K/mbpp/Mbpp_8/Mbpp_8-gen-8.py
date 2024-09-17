```
def square_nums(numbers):
    return [num ** 2 for num in numbers]
```


This function takes a list of numbers as input and returns a new list where each element is the square of the corresponding element in the input list. The expression `num ** 2` calculates the square of a number. The list comprehension `[num ** 2 for num in numbers]` creates a new list with these squared numbers. For example, `square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])` returns `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`.