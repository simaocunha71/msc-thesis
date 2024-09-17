```
def get_ludic(n):
    lucid_numbers = [i for i in range(1, n+1) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))]
    return lucid_numbers
```
The function `get_ludic` takes an integer `n` as input and returns a list of all lucid numbers smaller than or equal to `n`.

A lucid number is a number that has no divisors other than 1 and itself. To check if a number is lucid, we can iterate over all numbers from 2 to the square root of the number, and check if the number is divisible by any of them. If it is not divisible by any of them, then it is a lucid number.

In the function, we use a list comprehension to generate the list of lucid numbers. We iterate over all numbers from 1 to `n`, and for each number, we check if it is lucid by using the `all` function with a generator expression. The generator expression checks if the number is divisible by any number from 2 to the square root of the number. If the number is not divisible by any of these numbers, then it is a lucid number, and we add it to the list.

The unit test `assert get_ludic(10) == [1, 2, 3, 5, 7]` ensures that the function returns the correct list of lucid numbers for the input `10`. This test can be used to verify that the function is working correctly.