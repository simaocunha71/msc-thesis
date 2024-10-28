```
def Split(lst):
    return [i for i in lst if i % 2 == 0]
```
The function `Split` takes a list of numbers as input and returns a new list containing only the even numbers from the input list. The condition `i % 2 == 0` is used to check if a number is even. This is a common and efficient way to solve this problem in Python. 

The unit test `assert Split([1,2,3,4,5]) == [2,4]` helps to ensure that the function works correctly. It checks that the output of the function `Split([1,2,3,4,5])` is `[2,4]`, which is the expected result. This test can be run to verify that the function is working correctly. 





