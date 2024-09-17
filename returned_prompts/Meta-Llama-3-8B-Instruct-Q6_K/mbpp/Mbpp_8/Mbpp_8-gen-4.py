```
def square_nums(numbers):
    return [num**2 for num in numbers]
```
The function `square_nums` takes a list of numbers as input, and returns a new list where each element is the square of the corresponding element in the input list. The function uses a list comprehension to achieve this. The unit test provided ensures that the function works correctly for a list of integers from 1 to 10. 
For example, `square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])` returns `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`. 
This function can be used with lists of any type of numbers, not just integers. For example, `square_nums([1.0, 2.0, 3.0])` returns `[1.0, 4.0, 9.0]`. 
If the input list is empty, the function returns an empty list. For example, `square_nums([])` returns `[]`. 







