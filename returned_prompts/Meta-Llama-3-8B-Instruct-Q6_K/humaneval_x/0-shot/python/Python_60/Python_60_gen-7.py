```
def sum_to_n(n: int):
    return sum(range(1, n+1))
```


Explanation:
The problem asks to create a function `sum_to_n` that takes an integer `n` as input and returns the sum of all numbers from 1 to `n`. 

The unit tests provided help in understanding the expected behavior of the function. For example, `sum_to_n(30)` should return `465`, which is the sum of all numbers from 1 to 30.

To solve this problem, we can use the built-in `range` function in Python to generate a sequence of numbers from 1 to `n`, and then use the `sum` function to calculate the sum of these numbers.

Here is the solution:
```
def sum_to_n(n: int):
    return sum(range(1, n+1))
```
This function takes an integer `n` as input, generates a sequence of numbers from 1 to `n` using `range(1, n+1)`, and then returns the sum of these numbers using the `sum` function. The `+1` in `range(1, n+1)` is necessary because the `range` function is exclusive of the end value, so we need to include `n` in the sequence by adding 1. 

This function passes all the provided unit tests. For example, `sum_to_n(30)` returns `465`, `sum_to_n(100)` returns `5050`, `sum_to_n(5)` returns `15`, `sum_to_n(10)` returns `55`, and `sum_to_n(1)` returns `1`. 