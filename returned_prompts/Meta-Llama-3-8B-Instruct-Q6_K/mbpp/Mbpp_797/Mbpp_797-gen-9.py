```
def sum_in_range(l, r):
    return sum(i for i in range(l, r+1) if i % 2 != 0)
```
The function `sum_in_range` takes two parameters `l` and `r` which are the lower and upper bounds of the range. It uses a generator expression to iterate over the range from `l` to `r+1` (inclusive) and sums up all the numbers that are not divisible by 2 (i.e., odd numbers). The unit test `assert sum_in_range(2,5) == 8` helps to clarify the expected behavior of the function. 

The function works as follows:

- `range(l, r+1)` generates a sequence of numbers from `l` to `r` (inclusive).
- `i for i in range(l, r+1)` is a generator expression that iterates over the sequence of numbers.
- `if i % 2 != 0` is a filter that selects only the numbers that are not divisible by 2 (i.e., odd numbers).
- `sum(...)` adds up all the selected numbers. 

The function returns the sum of all odd natural numbers within the range `l` and `r`. 
```python
print(sum_in_range(2,5))  # Output: 8
``` 
The function works correctly for the given unit test and can be used to find the sum of all odd natural numbers within any given range. 