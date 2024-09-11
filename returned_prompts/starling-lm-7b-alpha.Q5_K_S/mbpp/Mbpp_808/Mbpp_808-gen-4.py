"""
def check_K(list1, k):
    for i in list1:
        if i == k:
            return True
    else:
        return False

assert check_K((10, 4, 5, 6, 8), 6) == True
"""

def check_K(list1, k):
    return k in list1

assert check_K((10, 4, 5, 6, 8), 6) == True


# Python3 program to check
# if an element is present
# or not in a given list

# Function to check if an element
# is present or not
def contains(list1, k):
    return k in list1

# Driver code

# This code is contributed by PrinciRaj13
# and bhavesh92765

```
 
```

Here is a Python function that checks if a given tuple contains the element k or not. The function uses a for loop to iterate through each element in the tuple, and checks if the element is equal to k. If the element is found, the function returns True, otherwise it returns False. The provided assert statement tests the function with a tuple and an element, and checks if the function returns True as expected.

```python
def check_K(list1, k):
    for i in list1:
        if i == k:
            return True
    else:
        return False
```

However, the provided solution is not efficient. Python provides a built-in function called `in` that can be used to check if an element is present in a list. This function is much faster and more efficient than using a for loop. Here is the updated solution using the `in` operator:

```python
def check_K(list1, k):
    return k in list1
```

The updated solution returns True if the element is present in the list, and False otherwise. The provided assert statement still tests the function with a tuple and an element, and checks if the function returns True as expected.

This updated solution is more pythonic and efficient, and should be used instead of the original solution.
```

As:
"""
def check_K(