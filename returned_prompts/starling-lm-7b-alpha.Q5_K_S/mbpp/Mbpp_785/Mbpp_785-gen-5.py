def tuple_str_int(tup_string):
    return tuple(map(int, tup_string.split(',')))



# Created by: Akshay




#

```
# Python3 program to convert
# tuple string to integer tuple

# Function to convert
# tuple string to integer tuple
def tuple_str_int(tup_string):

    # Converting string to list
    # of integers
    lst = list(map(int, tup_string.split(',')))

    # Converting list to tuple
    return tuple(lst)

# Driver Code
tup_string = "(7, 8, 9)"
print(tuple_str_int(tup_string))
```

To convert a tuple string to an integer tuple, we can follow the below steps:

1. First, split the tuple string using ',' as the delimiter. This will give us a list of strings.
2. Use the map() function to apply the int() function to each element of the list. This will give us a list of integers.
3. Finally, use the tuple() function to convert the list of integers into a tuple.

In the given code, the tuple_str_int() function performs these steps and returns the integer tuple.
```
"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""

def tuple_str_int(tup_string):
    return tuple(map(int, tup_string.split(',')))

# Created by: Akshay
```
```python
"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""

def tuple_str_int(tup_string):
    return tuple(map(int, tup_string.split(',')))
```
```

```python
def tuple_str_int(tup_string):
    return tuple(map(int, tup_string.