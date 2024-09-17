```
def square_nums(numbers):
    return [i**2 for i in numbers]
```
This function uses a list comprehension to square each element in the input list. The expression `i**2` squares each element `i` in the list, and the result is a new list containing the squares. The function returns this new list. 

For example, if the input list is `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, the function will return the list `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`. 

The unit test `assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` confirms that the function works correctly. 







