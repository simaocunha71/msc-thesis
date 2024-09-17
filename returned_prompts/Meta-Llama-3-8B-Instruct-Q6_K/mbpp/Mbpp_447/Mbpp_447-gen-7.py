```
def cube_nums(lst):
    return [i**3 for i in lst]
```
This function uses a list comprehension to iterate over each element in the input list, cube it (by raising it to the power of 3), and return a new list with the results.

The unit test provided ensures that the function works correctly:
```
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```


This test checks if the output of the function, when given the input list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], is equal to the expected list [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]. If the output matches the expected result, the test passes. If not, the test fails.