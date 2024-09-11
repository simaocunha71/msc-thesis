"""
Here's one possible solution to this problem:

```python
def index_minimum(t):
    minimum = t[0][1]
    for i in range(1, len(t)):
        if t[i][1] < minimum:
            minimum = t[i][1]
            index = i
    return t[index][0]
```

This function, index_minimum, first initializes a variable, minimum, to the first tuple's second value. Then it iterates through the list of tuples, comparing each tuple's second value to the current minimum value. If it finds a tuple with a smaller second value, it updates both the minimum and the index of that tuple. Finally, it returns the first value of the tuple with the smallest second value.

For the given example, the function would return 'Varsha' because the tuple ('Varsha', 100) has the smallest second value (100) of all the tuples in the list.

Here's a step-by-step breakdown of how the function works for the given example:

1. Initialize minimum to 143 (the second value of the first tuple).
2. Compare the second value of the second tuple (200) to minimum. Since 200 is greater than 143, minimum remains 143 and index remains 0.
3. Compare the second value of the third tuple (100) to minimum. Since 100 is less than 143, minimum becomes 100 and index becomes 1.
4. Since there are no more tuples to compare, the function returns the first value of the tuple with the smallest second value, which is 'Varsha'.
"""

def index_minimum(t):
    minimum = t[0][1]
    for i in range(1, len(t)):
        if t[i][1] < minimum:
            minimum = t[i][1]
            index = i
    return t[index][0]

# Test the function with the given example
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'