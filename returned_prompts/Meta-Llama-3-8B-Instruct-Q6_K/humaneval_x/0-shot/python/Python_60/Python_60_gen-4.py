def sum_to_n(n: int):
    return sum(range(1, n + 1))
    # or
    # return sum(i for i in range(1, n + 1))
    # or
    # result = 0
    # for i in range(1, n + 1):
    #     result += i
    # return result
    # or
    # return n * (n + 1) // 2  # formula for sum of an arithmetic series

print(sum_to_n(30))  # 465
print(sum_to_n(100))  # 5050
print(sum_to_n(5))    # 15
print(sum_to_n(10))   # 55
print(sum_to_n(1))    # 1
    



The task is to write a function called `sum_to_n` that calculates the sum of all numbers from 1 to `n`, inclusive. The function should take an integer `n` as input and return the sum.

The provided unit tests demonstrate the expected output for different values of `n`. For example, `sum_to_n(30)` should return `465`, `sum_to_n(100)` should return `5050`, and so on.

Here's a simple solution using the built-in `sum` function and the `range` function:
```python
def sum_to_n(n: int):
    return sum(range(1, n + 1))
```
This function uses the `range` function to generate a sequence of numbers from 1 to `n` (inclusive), and then passes that sequence to the `sum` function to calculate the sum.

Alternatively, you can use a generator expression or a for loop to achieve the same result:
```python
def sum_to_n(n: int):
    return sum(i for i in range(1, n + 1))
```
or
```python
def sum_to_n(n: int):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result
```
Finally, you can use the formula for the sum of an arithmetic series to calculate the result:
```python
def sum_to_n(n: int):
    return n * (n + 1) // 2
```
This formula is more efficient than the other solutions, especially for large values of `n`.