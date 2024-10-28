```
def cube_nums(lst):
    return [i ** 3 for i in lst]
```
The function `cube_nums` takes a list of numbers as input and returns a new list where each element is the cube of the corresponding element in the input list. The `**` operator is used to calculate the cube of a number. 

The unit test `assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]` ensures that the function works correctly by comparing the result with the expected output. 