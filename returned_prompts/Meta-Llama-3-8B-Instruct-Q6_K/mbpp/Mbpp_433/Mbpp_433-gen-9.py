```
def check_greater(arr, num):
    return all(num > x for x in arr)
```
The function check_greater takes two parameters: an array and a number. It uses the built-in all function in Python, which returns True if all elements of the iterable (in this case, a generator expression) are True. The generator expression num > x for x in arr checks if the given number is greater than each element in the array. If the number is not greater than all elements in the array, the function returns False. If the number is greater than all elements in the array, the function returns True. 

For example, when you call check_greater([1, 2, 3, 4, 5], 4), the function returns False because 4 is not greater than all elements in the array. 

This function assumes that the array is not empty. If the array can be empty, you should add a check for this case, for example, return False if len(arr) == 0. 

The unit test provided, assert check_greater([1, 2, 3, 4, 5], 4) == False, passes because the given number 4 is not greater than all elements in the array. 
```python
assert check_greater([1, 2, 3, 4, 5], 4) == False
```  ```python
def check_greater(arr, num):
    return all(num > x for x in arr)
``` 
The function check_greater takes two parameters: an array and a number. It uses the built-in all function in Python, which returns True if all elements of the iterable (in this case, a generator expression) are True. The generator expression num > x for x in arr checks if the given number is greater than each element in the array. If the number is not greater than all elements in the array, the function returns False. If the number is greater than all elements in the array, the function returns True. 

For example, when you call check_greater([1, 2, 3, 4, 5], 4), the function returns False because 4 is not greater than all elements in the array. 

This function assumes that the array is not empty. If the array can be empty, you should add a check for this case, for example, return False if len(arr) == 0. 

The unit test provided, assert check_greater([1, 2