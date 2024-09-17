```
def square_nums(lst):
    return [num ** 2 for num in lst]
```
This function uses a list comprehension to square each number in the input list. The `**` operator is used to raise each number to the power of 2, effectively squaring it. The resulting list of squares is then returned. The unit test provided ensures that the function works correctly for the given input. For example, `square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])` should return `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`.