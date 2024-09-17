You can solve this problem with the following function:

```python
def smallest_num(lst):
  return min(lst)
```


This function takes a list of numbers as an argument and returns the smallest number in the list. It does this by using the built-in min function in Python, which returns the smallest item in an iterable or the smallest of two or more arguments. In this case, the iterable is the list of numbers. The function is tested with the unit test `assert smallest_num([10, 20, 1, 45, 99]) == 1`, which ensures that the function works as expected. The function should work with lists of any size, and it should return the smallest number in the list. If the list is empty, the function will raise a ValueError. If you want to handle this case, you can add a check at the beginning of the function to return a specific value (for example, None) if the list is empty. Here's how you can do it:

```python
def smallest_num(lst):
  if not lst:
    return None
  return min(lst)
```


In this version of the function, the function returns None if the list is empty. The function still works as expected with non-empty lists, and it raises a ValueError if the list contains non-numeric values. If you want to handle this case, you can add a check at the beginning of the function to return a specific value (for example, None) if the list contains non-numeric values. Here's how you can do it:

```python
def smallest_num(lst):
  if not lst:
    return None
  if not all(isinstance(x, int) for x in lst):
    return None
  return min(lst)
```


In this version of the function, the function returns None if the list is empty or if the list contains non-numeric values. The function still works as expected with lists of numeric values. The function will raise a ValueError if the list contains non-numeric values. If you want to handle this case, you can add a try/except block to catch the ValueError and return a specific value (for example, None) if the list contains non-numeric values. Here's how you can do it:

```python
def smallest_num(lst):
  if not lst:
    return None
  try:
    return min(lst)
  except TypeError:
    return None
```


In this version of the function, the function returns None if the list is empty or