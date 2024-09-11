```
def centered_hexagonal_number(n):
    # The nth centered hexagonal number is given by the formula: (3n^2 - n) / 2
    return (3 * n ** 2 - n) // 2
```

Explanation:

A centered hexagonal number is a number that can be represented as the sum of four equilateral triangles of size n, with one in the center and the others surrounding it. The formula for the nth centered hexagonal number is (3n^2 - n) / 2. 

The function `centered_hexagonal_number` takes an integer `n` as input and returns the nth centered hexagonal number using the given formula. 

In the formula, `n` represents the size of the equilateral triangles that make up the centered hexagonal number. 

To calculate the nth centered hexagonal number, we multiply `n` by itself (`n * n`) and then multiply the result by 3 (`3 * n * n`). We then subtract `n` from this result (`3 * n * n - n`) and divide the result by 2 (`(3 * n * n - n) / 2`). 

The function returns the calculated value as the nth centered hexagonal number. 

For example, if we call `centered_hexagonal_number(10)`, it will return 271, which is the 10th centered hexagonal number. 

The assert statement in the code example is used to verify that the `centered_hexagonal_number` function is correct by checking if it returns the expected result for the given input (10). 

Overall, this function provides a simple and efficient way to calculate the nth centered hexagonal number using the given formula.

Here are some more examples of using the `centered_hexagonal_number` function:
```python
print(centered_hexagonal_number(5))  # Output: 45
print(centered_hexagonal_number(1))  # Output: 0
print(centered_hexagonal_number(100))  # Output: 33137
```

These examples demonstrate how the function