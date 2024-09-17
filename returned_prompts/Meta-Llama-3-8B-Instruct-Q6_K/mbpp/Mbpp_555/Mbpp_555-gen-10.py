```
def difference(n):
    sum_cubes = sum(i**3 for i in range(1, n+1))
    sum_natural = (n * (n + 1)) // 2
    return sum_cubes - sum_natural
```


The problem is asking to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers. 

The sum of cubes of the first n natural numbers can be calculated using the formula `sum(i**3 for i in range(1, n+1))`.

The sum of the first n natural numbers can be calculated using the formula `(n * (n + 1)) // 2`.

So, the function would be:
```
def difference(n):
    sum_cubes = sum(i**3 for i in range(1, n+1))
    sum_natural = (n * (n + 1)) // 2
    return sum_cubes - sum_natural
```
This function takes an integer `n` as input and returns the difference between the sum of cubes of the first `n` natural numbers and the sum of the first `n` natural numbers. 

The unit test `assert difference(3) == 30` ensures that the function returns the correct result for `n=3`. 

For example, for `n=3`, the sum of cubes of the first 3 natural numbers is `1**3 + 2**3 + 3**3 = 1 + 8 + 27 = 36`, and the sum of the first 3 natural numbers is `(3 * (3 + 1)) // 2 = 6`. So, the difference is `36 - 6 = 30`. 

The function will return `30` for `n=3`, which passes the unit test. 