The function `sum_to_n` calculates the sum of all numbers from 1 to `n` using a simple loop.
Here is the Python code for the function:
```python
def sum_to_n(n: int):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```
This function iterates over the range from 1 to `n` (inclusive) and adds each number to a running total. The final total is returned as the result. The function is tested with various inputs to demonstrate its correctness.