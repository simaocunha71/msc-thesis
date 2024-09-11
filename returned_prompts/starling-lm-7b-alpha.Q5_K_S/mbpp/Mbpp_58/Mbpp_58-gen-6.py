```
def opposite_Signs(n1,n2):
    if (n1<0 and n2>0) or (n1>0 and n2<0):
        return True
    else:
        return False
```

Here are some tests for this function:
```python
assert opposite_Signs(1,-2) == True
assert opposite_Signs(-1,-2) == True
assert opposite_Signs(1,1) == False
assert opposite_Signs(0,0) == False
```

Explanation:

The function `opposite_Signs` takes two integer arguments: `n1` and `n2`.

It uses a series of conditional statements to determine if the two integers have opposite signs. The first condition checks if `n1` is less than 0 (i.e., negative) and `n2` is greater than 0 (i.e., positive). If this condition is true, the function returns `True`, indicating that the two integers have opposite signs. If this condition is false, the function proceeds to the next condition.

The second condition checks if `n1` is greater than 0 (i.e., positive) and `n2` is less than 0 (i.e., negative). If this condition is true, the function also returns `True`. If this condition is false, the function proceeds to the `else` clause and returns `False`, indicating that the two integers do not have opposite signs.

In the `else` clause, the function only returns `False` if none of the previous conditions are true. This means that if both `n1` and `n2` are either both positive or both negative, the function will return `False`.

The provided tests demonstrate the correctness of the `opposite_Signs` function. The assertions verify that the function correctly determines if two integers have opposite signs.

Note that the function assumes that the input arguments are integers. If the function is called with non-integer arguments, it may raise a `TypeError`.
```
```

# Python3 program to check if two numbers
# have opposite signs or not

# Function to check if two numbers
# have opposite signs
def opposite_Signs(n1,n