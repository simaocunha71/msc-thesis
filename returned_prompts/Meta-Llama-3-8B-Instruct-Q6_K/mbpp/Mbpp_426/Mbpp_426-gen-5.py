```
def filter_oddnumbers(numbers):
    return [num for num in numbers if num % 2 != 0]
```
This function uses a list comprehension to create a new list that includes only the numbers from the input list that are odd. The condition `num % 2 != 0` is used to check if a number is odd. The unit test `assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]` shows that this function works correctly. 