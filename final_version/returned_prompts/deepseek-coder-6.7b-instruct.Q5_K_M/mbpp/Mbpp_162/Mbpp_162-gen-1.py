Here is the Python code to solve the problem:

```python
def sum_series(n):
    total = 0
    i = 0
    while n - 2*i > 0:
        total += n - 2*i
        i += 1
    return total

print(sum_series(6))  # Output: 12
```
This function works by iterating through the range of values from 0 to n // 2, and for each iteration, it adds the value (n - 2*i) to the total. The loop continues until (n - 2*i) is less than or equal to 0.

Please note that the range of values from 0 to n // 2 is determined by the condition n - 2*i > 0. This is because for each iteration, we subtract 2*i from n. When 2*i becomes greater than n, the condition n - 2*i will be less than or equal to 0, and the loop will terminate.

The time complexity of this function is O(n) because it makes a single pass through the range of values from 0 to n // 2. The space complexity is O(1) because it uses a constant amount of space to store the total and the counter variable i.
"""

