"""
def count_divisors(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    return c

def check_divisors(n):
    c = count_divisors(n)
    return c % 2 == 0

print(check_divisors(10))
"""

Here is a python function that checks whether the count of divisors of a given number is even or not. It calls the `count_divisors` function to count the divisors of the number and returns `True` if the count is even and `False` if the count is odd:

```python
def count_divisors(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    return c

def check_divisors(n):
    c = count_divisors(n)
    return c % 2 == 0
```

To use this function, you can pass the number you want to check as an argument to the `check_divisors` function. For example, to check whether the count of divisors of 10 is even, you can call `check_divisors(10)`. The function will return `True` because the count of divisors of 10 (which is 4) is even:

```python
print(check_divisors(10))  # prints: True
```

This function can be used to check whether the count of divisors of any given number is even or not.

```python
check_divisors(15)  # prints: False
```

In this case, the count of divisors of 15 (which is 5) is odd, so the function returns `False`.

```python
check_divisors(20)  # prints: True
```

Here, the count of divisors of 20 (which is 8) is even, so the function returns `True`.

```python
check_divisors(21) 