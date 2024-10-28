
To find the largest divisor of a number, we can iterate through all the numbers from 2 to the number itself and check if the number is divisible by that number or not. If it's divisible, we return that number. Otherwise, we move to the next number. Here is the step-by-step process:

1. Initialize a variable `largest` to 1. This will hold the largest divisor we find.
2. Iterate through all the numbers from 2 to `n`. For each number, check if `n` is divisible by it using the modulo operator `%`. If the remainder is 0, it means `n` is divisible by that number, so we update `largest` to that number.
3. After iterating through all the numbers, return the value of `largest`.

Here's the Python code that implements the above steps:

```python
def largest_divisor(n: int) -> int:
    largest = 1
    for i in range(2, n):
        if n % i == 0:
            largest = i
    return largest
```

This function will return the largest divisor of the given number. For example, if you call `largest_divisor(15)`, it will return 5, as 5 is the largest number that divides 15 evenly.

Note: This implementation assumes that the input `n` is always a positive integer. If you want to handle negative numbers or zero as well, you can add appropriate error checking in the function.

I hope this helps! Let me know if you have any more questions.

```python

```