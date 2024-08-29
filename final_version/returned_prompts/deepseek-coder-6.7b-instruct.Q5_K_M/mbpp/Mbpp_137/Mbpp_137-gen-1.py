Here is the Python code to solve the problem:

```python
def zero_count(arr):
    zero_counter = 0
    non_zero_counter = 0
    
    for num in arr:
        if num == 0:
            zero_counter += 1
        else:
            non_zero_counter += 1
            
    return zero_counter / non_zero_counter
```

Test the function:

```python
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
```

The function `zero_count` takes an array of integers as input, counts the number of zeros and non-zeros in the array, and then returns the ratio of zeros to non-zeros.

The `math.isclose()` function is used to check if the output of the function is close to the expected output within a relative tolerance of 0.001.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
3. Python Programming: Convert List to Dictionary
<jupyter_code>
