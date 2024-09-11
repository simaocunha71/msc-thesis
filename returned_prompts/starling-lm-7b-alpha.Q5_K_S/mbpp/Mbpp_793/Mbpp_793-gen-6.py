Here is one way you might implement this function:

```python
def last(lst, x):
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == x:
            return i
    return -1
```

This function starts from the end of the array and checks each element in turn until it finds the first one that matches the target value.

The function also includes a special return value of -1 to indicate that the target value was not found in the array.

Here's a test case with the expected output:

```python
print(last([1,2,3],1))  # prints: 0
```

This test case checks that the target value of 1 is found at the start of the array (position 0).

Here's a test case for a value that is not in the array:

```python
print(last([1,2,3],4))  # prints: -1
```

This test case checks that the target value of 4 is not found in the array, and returns the special return value of -1 to indicate this.

```python
def last(lst, x):
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == x:
            return i
    return -1
```

This function iterates through the list from the end to the beginning, starting with the index of the last element in the list. It checks each element in turn until it finds the first one that matches the target value. If it doesn't find the target value, it returns -1 to indicate that the target value was not found in the array.

Here are some test cases to validate the function:

```python
assert last([1,2,3],1) == 0  # true
assert last([1,2,3],4) == -1  # true
```

These test cases check that the function correctly returns the index of the first occurrence of the target value, or -1 if the target value is not found.

```python
print(last([1,2,3],1))  # prints: 0
print(last([1