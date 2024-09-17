```
def sum_in_range(l, r):
    return sum(i for i in range(l, r+1) if i % 2 != 0)
```
Explanation: 
The function `sum_in_range` takes two parameters `l` and `r` representing the lower and upper bounds of the range respectively. It uses a generator expression to iterate over the range `l` to `r` (inclusive) and filters out even numbers using the condition `i % 2 != 0` which is true for odd numbers. The sum of these odd numbers is then returned. The unit test `assert sum_in_range(2,5) == 8` ensures that the function works correctly. 

The `range(l, r+1)` generates numbers from `l` to `r` inclusive. The `i for i in range(l, r+1)` is a generator expression that iterates over the range. The `if i % 2 != 0` is a filter that only includes odd numbers in the sum. The `sum` function then adds up all these odd numbers. 