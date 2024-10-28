```
def cube_nums(lst):
    return [i**3 for i in lst]
```
This function uses a list comprehension to create a new list where each element is the cube of the corresponding element in the input list. For example, if the input list is `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, the output will be `[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]`. 

The unit test provided ensures that the function works correctly. The test checks that the output of the function is the same as the expected output when the input is a list of numbers from 1 to 10. 

This function can be used to find the cubes of individual elements in any list of numbers. It's a simple and efficient way to perform this operation. 