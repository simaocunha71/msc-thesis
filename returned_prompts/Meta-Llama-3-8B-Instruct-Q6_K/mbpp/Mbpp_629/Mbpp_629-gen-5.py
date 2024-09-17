```
def Split(lst):
    return [num for num in lst if num % 2 == 0]
```


This function uses a list comprehension to iterate over each number in the input list `lst`. It checks if the number is even by using the modulus operator `%` to find the remainder when the number is divided by 2. If the remainder is 0, the number is even, and it is included in the output list. The function returns the list of even numbers. The unit test `assert Split([1,2,3,4,5]) == [2,4]` ensures that the function works correctly.