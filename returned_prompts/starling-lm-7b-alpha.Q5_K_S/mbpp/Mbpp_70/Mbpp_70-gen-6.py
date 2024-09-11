```python
def get_equal(tuples_list):
    len_list = []
    for i in range(len(tuples_list)):
        len_list.append(len(tuples_list[i]))
    if len(set(len_list)) == 1:
        return True
    else:
        return False
```

In the above function, we are getting the length of all the tuples in the given list. Then, we are storing all the lengths in a list. If the number of different lengths in that list is equal to 1, it means all the given tuples have the same length, else not.

To check the function, we can use the below provided assert statement.

```python
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
```

The above assert statement will return True if the function correctly identifies whether the lengths of all tuples in the list are equal or not, else it will return False.

```python
def get_equal(tuples_list):
    len_list = []
    for i in range(len(tuples_list)):
        len_list.append(len(tuples_list[i]))
    if len(set(len_list)) == 1:
        return True
    else:
        return False
```

The above function will return True if all the given tuples have the same length, else it will return False.

```python
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
```

The above assert statement can be used to verify if the function correctly identifies whether the lengths of the given tuples are equal or not.

```python
def get_equal(tuples_list):
    len_list = []
    for i in range(len(tuples_list)):
        len_list.append(len(tuples_list[i]))
    if len(set(len_list)) == 1:
        return True
    else:
        return False
```

The above function is a solution