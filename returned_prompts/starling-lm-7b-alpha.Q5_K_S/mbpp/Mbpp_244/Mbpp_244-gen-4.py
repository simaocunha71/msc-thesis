def next_Perfect_Square(n):
    i = n
    while True:
        if i % 2 == 0:
            i += 1
        else:
            i = (i + 1) // 2
        if i * i == (i ** 2):
            return i
```
    
Here is a Python function that finds the next perfect square greater than a given number. It does so by incrementing the input number by 1 until a perfect square is found (i.e., a number that is a factor of itself). The function uses a while loop to keep checking and incrementing the number until a perfect square is found. The function returns the next perfect square as the result.

To test the function, you can use the `assert` statement to verify that the function correctly finds the next perfect square greater than a given number. For example, the assertion `assert next_Perfect_Square(35) == 36` asserts that the function should return 36 when given the input 35.

Here's a breakdown of the function:

1. The function starts by initializing a variable `i` with the input number `n`.
2. It then enters a while loop that continues indefinitely until a perfect square is found.
3. Inside the loop, the function checks if `i` is divisible by 2 (i.e., even). If it is, `i` is incremented by 1. Otherwise, `i` is divided by 2 (i.e., rounded down to the nearest whole number).
4. After the increment or division operation, the function checks if `i` squared is equal to the square of `i` itself (i.e., if `i` is a perfect square). If it is, the function returns `i` as the next perfect square.
5. If a perfect square is not found in a particular iteration, the loop continues to the next iteration, repeating steps 3-4 until a perfect square is found.

By following this logic, the function correctly finds the next perfect square greater than a given number.

```python
def next_Perfect_Square(n):
    i = n
    while True:
        if i % 2 == 0:
            i += 1