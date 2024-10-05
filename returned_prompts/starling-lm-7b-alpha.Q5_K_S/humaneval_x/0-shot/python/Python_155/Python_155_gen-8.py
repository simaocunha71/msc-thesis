
The function `even_odd_count` takes an integer as input and returns a tuple with the number of even and odd digits respectively.

Here's the step-by-step explanation:

1. The function `even_odd_count` takes a parameter `num`, which is the input integer.
2. The function uses the built-in `map` function to apply the modulo operator `%` to each digit of the input integer. The modulo operator `%` returns the remainder of the division of two numbers. In this case, it will return 0 if the number is even and 1 if the number is odd.
3. The `map` function is used to convert the result of the modulo operation into a list of booleans. `True` represents an odd number and `False` represents an even number.
4. The `len` function is used to count the number of `True` values (odd numbers) and `False` values (even numbers) in the list.
5. The `len` function is used again to count the number of `False` values (even numbers) in the list.
6. The `len` function is used again to count the number of `True` values (odd numbers) in the list.
7. The `len` function is used again to count the number of `False` values (even numbers) in the list.
8. The function returns a tuple with the number of even and odd digits respectively.

Here's an example usage of the `even_odd_count` function:

```python
result = even_odd_count(-12)
print(result)  # Output: (1, 1)
```

In this example, the function is called with the input `-12`. The function counts that there is one even digit and one odd digit in the number, and returns the tuple `(1, 1)`.

```python
result = even_odd_count(123)
print(result)  # Output: (1, 2)
```

In this example, the function is called with the input `123`. The function counts that there is one even digit and two odd digits in the number, and returns the tuple `(1, 2)`.

```python
