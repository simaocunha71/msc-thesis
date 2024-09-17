```
def get_ludic(n):
    lucid_numbers = [i for i in range(1, n+1) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))]
    return lucid_numbers
```


This function generates all lucid numbers smaller than or equal to the given integer `n`. A lucid number is a number that has no divisors other than 1 and itself.

The function uses a list comprehension to generate all numbers from 1 to `n` and checks each number to see if it is lucid. A number is considered lucid if it is not divisible by any number between 2 and the square root of the number (inclusive). This is done using the `all` function, which returns `True` if all elements of the given iterable are true. The iterable in this case is a generator expression that yields `True` for each number `j` in the range from 2 to the square root of `i` (inclusive) if `i` is not divisible by `j`, and `False` otherwise.

The function returns a list of all lucid numbers found. For example, `get_lucid(10)` returns `[1, 2, 3, 5, 7]`. This is because these are the only numbers smaller than or equal to 10 that have no divisors other than 1 and themselves.