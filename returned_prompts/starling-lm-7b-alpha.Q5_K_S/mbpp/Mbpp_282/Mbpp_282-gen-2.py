"""
def sub_list(list1, list2):
    if len(list1) != len(list2):
        return None
    else:
        return [list1[i] - list2[i] for i in range(len(list1))]

# Testing
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
print("All tests passed")
"""

# Here's a version that uses built-in Python functions
def sub_list(list1, list2):
    if len(list1) != len(list2):
        return None
    else:
        return [x-y for x,y in zip(list1, list2)]

# Testing
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
print("All tests passed")














"""
"""

```
def sub_list(list1, list2):
    if len(list1) != len(list2):
        return None
    else:
        result = []
        for i in range(len(list1)):
            result.append(list1[i] - list2[i])
        return result

# Testing
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
print("All tests passed")
```

```python
def sub_list(list1, list2):
    if len(list1) != len(list2):
        return None
    else:
        return [list1[i] - list2[i] for i in range(len(list1))]

# Testing
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
print("All tests passed")
```
"""
```python
def sub_list(list1, list2):
    if len(list1) != len(list2):
        return None
    else:
        return [list1[i] - list