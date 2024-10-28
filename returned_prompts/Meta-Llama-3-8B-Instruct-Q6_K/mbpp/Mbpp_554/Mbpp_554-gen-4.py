```
def Split(lst):
    return [i for i in lst if i % 2 != 0]
```
The function `Split` takes a list `lst` as an argument. It uses a list comprehension to create a new list that includes only the elements from `lst` that are not divisible by 2. The condition `i % 2 != 0` is used to check if a number is odd. This function will return a list of all the odd numbers from the input list.

The unit test `assert Split([1,2,3,4,5,6]) == [1,3,5]` ensures that the function is working correctly. It checks that the function returns the list `[1,3,5]` when given the input list `[1,2,3,4,5,6]`. This is because these are the only odd numbers in the input list. If the function is working correctly, the unit test will pass without raising an AssertionError. 