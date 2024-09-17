You can use the built-in `min` function in Python, which returns the smallest item in an iterable or the smallest of two or more arguments. In this case, you can use `min` with a generator expression that converts all items to numbers:

```python
def find_min(lst):
    return min(num for num in lst if isinstance(num, (int, float)))
```

This function will return the smallest integer or float in the list. If the list contains only strings, it will raise a ValueError. If you want to handle this case, you can add a condition to return the smallest string if the list contains only strings:

```python
def find_min(lst):
    nums = [num for num in lst if isinstance(num, (int, float))]
    if nums:
        return min(nums)
    else:
        return min(lst)
```

This function will return the smallest integer or float in the list if it contains any. If the list contains only strings, it will return the smallest string. If the list is empty, it will raise a ValueError. You can handle this case by returning a default value, for example:

```python
def find_min(lst):
    nums = [num for num in lst if isinstance(num, (int, float))]
    if nums:
        return min(nums)
    else:
        return None
```  # or any other default value
```python
assert find_min(['Python', 3, 2, 4, 5, 'version'])==2
```  # should return 2
```python
assert find_min(['Python', 'version'])== 'Python'  # should return 'Python'
```  # or any other default value
```python
assert find_min([]) is None  # should return None
```  # or any other default value
```python
assert find_min([1, 2, 3, 4, 5]) == 1  # should return 1
```python
assert find_min([-1, -2, -3, -4, -5]) == -5  # should return -5
```python
assert find_min([1.5, 2.5, 3.5, 4.5, 5.5]) == 1.5  # should return 1.5
```python
assert find_min(['-1', '-2', '-3', '-4', '-5']) == '-5'  # should return '-