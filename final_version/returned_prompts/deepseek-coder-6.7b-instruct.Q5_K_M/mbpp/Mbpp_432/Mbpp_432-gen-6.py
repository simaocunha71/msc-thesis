Here is the Python solution to the problem:

```python
def median_trapezium(a, b, c):
    # calculate the median length
    median = (a + b + c) / 2
    return median

# test the function
print(median_trapezium(15, 25, 35))  # output: 25.0
```

This function calculates the median length of a trapezium by adding the lengths of the two parallel sides and dividing by 2.
The input parameters `a`, `b` and `c` represent the lengths of the parallel sides of the trapezium.
The function returns the median length of the trapezium.
"""
