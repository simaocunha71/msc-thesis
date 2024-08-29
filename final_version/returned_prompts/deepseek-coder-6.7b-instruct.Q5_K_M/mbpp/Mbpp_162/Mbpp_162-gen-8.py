"""
The function `sum_series` takes an integer `n` as an argument and calculates the sum of the series (n - 2*i) from i=0 to n//2. 

Here is the python code that implements the `sum_series` function:

```python
def sum_series(n):
    total_sum = 0
    for i in range(n//2+1):
        total_sum += n - 2*i
    return total_sum
```

Here we are using a for loop to iterate from 0 to n//2 and for each iteration we add the value (n - 2*i) to the `total_sum`. 

Finally we return the `total_sum`.

Now let's test the function with the provided test case:

```python
print(sum_series(6))  # Output: 12
```

The output of the program is 12 which is the correct answer.
"""

