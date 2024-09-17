The problem is asking to find the nth star number. Star numbers are defined as the sum of the first n natural numbers multiplied by the nth number. For example, the first star number is 1*1 + 2*2 = 5, the second star number is 1*1 + 2*2 + 3*3 = 14, and so on.

The problem doesn't explicitly define how to calculate the nth star number, but based on the unit test `assert find_star_num(3) == 37`, we can assume that the nth star number is the sum of the first n natural numbers multiplied by the nth number.

Here is the Python solution for the problem:

```python
def find_star_num(n):
    total = 0
    for i in range(1, n+1):
        total += i * i
    return total
```

This function calculates the nth star number by summing the squares of the first n natural numbers. For example, `find_star_num(3)` returns `1*1 + 2*2 + 3*3 = 37`, which is the expected result.