```
def opposite_Signs(a,b):
    if (a>0 and b<0) or (a<0 and b>0):
        return True
    else:
        return False
```

Explanation:
Here, the function `opposite_Signs` takes two arguments `a` and `b`. It checks if the signs of the two arguments are opposite of each other. If the first argument is positive and the second argument is negative, or if the first argument is negative and the second argument is positive, then the function returns True. Otherwise, it returns False.

For example, if we call the function `opposite_Signs(1,-2)`, it returns True because the signs of the two arguments are opposite of each other.

Note: In Python, a number is considered positive if it is greater than 0, and negative if it is less than 0.

The `assert` statement in the solution is used to verify the correctness of the function. It checks if the function returns True when given the arguments 1 and -2, and raises an error if the condition is not met.

This solution can be used to check whether two integers have opposite signs or not in Python.

Here are some additional examples of how you can use the `opposite_Signs` function:

```python
print(opposite_Signs(5,-3))  # Output: True
print(opposite_Signs(-4,2))  # Output: True
print(opposite_Signs(0,0))   # Output: False
print(opposite_Signs(3,1))   # Output: False
```

In these examples, the function returns True when the signs of the arguments are opposite, and False when the signs are the same.

I hope this helps! Let me know if you have any more questions.
```

asked by: Karthik Sekar

Answer Rating:

1

Last Modified: 2 months ago

### Popular Now

1. 1

A Python function is missing its return statement. It should return the sum of two parameters. How can this be fixed?
2. 2

I have a list of lists and I want to find the index of the list that