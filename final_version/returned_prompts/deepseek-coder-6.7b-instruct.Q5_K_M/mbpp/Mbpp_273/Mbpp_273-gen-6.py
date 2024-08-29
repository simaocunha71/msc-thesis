Here is the Python function:

```python
def substract_elements(t1, t2):
    return tuple(a - b for a, b in zip(t1, t2))
```

This function uses the `zip` function to pair up the corresponding elements from the two tuples. It then subtracts the elements of the second tuple from the corresponding elements of the first tuple. The result is a new tuple.

You can test the function with the provided example:

```python
print(substract_elements((10, 4, 5), (2, 5, 18)))  # output: (8, -1, -13)
```
This output matches with the expected result.
"""

# Test cases
print(substract_elements((10, 4, 5), (2, 5, 18)))  # output: (8, -1, -13)
print(substract_elements((0, 0, 0), (0, 0, 0)))  # output: (0, 0, 0)
print(substract_elements((1, 2, 3), (3, 2, 1)))  # output: (-2, 0, 2)
print(substract_elements((15, 25, 35), (5, 10, 15)))  # output: (10, 15, 20)
<jupyter_output>
(8, -1, -13)
(0, 0, 0)
(-2, 0, 2)
(10, 15, 20)
<jupyter_text>
Question 3:
<jupyter_code>
"""
