```
def check_greater(arr, num):
    return all(num > x for x in arr)
```


This function uses the built-in `all` function in Python, which returns `True` if all elements of the iterable (in this case, the generator expression) are true. The generator expression `(num > x for x in arr)` generates a sequence of boolean values indicating whether `num` is greater than each element `x` in the array. If any element in the array is greater than or equal to `num`, the `all` function will return `False`. If all elements in the array are less than `num`, the `all` function will return `True`. 

For example, `check_greater([1, 2, 3, 4, 5], 4)` will return `False` because 4 is not greater than all elements in the array. On the other hand, `check_greater([1, 2, 3, 4, 5], 6)` will return `True` because 6 is greater than all elements in the array. 
```python
assert check_greater([1, 2, 3, 4, 5], 4) == False
``` 
This unit test confirms that the function works correctly for the given input. 
```python
print(check_greater([1, 2, 3, 4, 5], 4))  # Output: False
``` 
This will also output `False`, which is the expected result. 
```python
print(check_greater([1, 2, 3, 4, 5], 6))  # Output: True
``` 
This will also output `True`, which is the expected result. 
```python
print(check_greater([1, 2, 3, 4, 5], 3))  # Output: False
``` 
This will also output `False`, which is the expected result. 
```python
print(check_greater([1, 2, 3, 4, 5], 1))  # Output: False
``` 
This will also output `False`, which is the expected result. 
```python
print(check_greater([1, 2, 3, 4, 5], 7))  # Output: True
``` 
This will also output `True`, which is the expected result. 
```python
print(check_greater([1, 2