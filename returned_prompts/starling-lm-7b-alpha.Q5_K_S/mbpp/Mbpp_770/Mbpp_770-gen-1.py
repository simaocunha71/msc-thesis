"""
def odd_num_sum(n):
    # Initialize result
    res = 0
    # Add squares of first n odd numbers
    for i in range(1, 2*n+1, 2):
        res += i**4
    return res
"""


def odd_num_sum(n):
    # Initialize result
    res = 0
    # Add squares of first n odd numbers
    for i in range(1, 2*n+1, 2):
        res += i**4
    return res

if __name__ == '__main__':
    print(odd_num_sum(2))

```
This Python function `odd_num_sum` takes an integer `n` as input and calculates the sum of the fourth powers of the first `n` odd natural numbers. The function uses a for loop to iterate through the odd numbers from 1 to 2*n+1 (inclusive) and adds their squares to the result variable `res`. Finally, the function returns the calculated sum.

In the provided code, the function `odd_num_sum` is called with `n=2` as an argument, and the result is printed to the console. The expected output is 82, as the sum of the fourth powers of the first two odd natural numbers (1 and 3) is 82.

Note that the range in the for loop starts from 1 and increments by 2 to only include odd numbers. The loop runs until `2*n+1` to include all odd numbers up to the `n`th odd number.

Overall, this function provides a straightforward solution to calculate the sum of the fourth powers of the first `n` odd natural numbers in Python.



```python
"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""

def odd_num_sum(n):
    # Initialize result
    res = 0
    # Add squares of first n odd numbers
    for i in range(1, 2*n+1, 2):
        res += i**4
    return res

if __name__ == '__