```
def cube_nums(lst):
    return [num**3 for num in lst]
```
The problem asks you to create a function that takes a list of numbers as input and returns a new list where each number is cubed (i.e., raised to the power of 3).

The unit test provided suggests that the input list is a list of integers, and the function should cube each integer and return the resulting list. For example, the input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] should return [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000].

The solution uses a list comprehension to iterate over the input list, cube each number using the ** operator, and return the resulting list. The function is defined as `cube_nums(lst)`, where `lst` is the input list. The unit test provided ensures that the function works correctly for the given input.