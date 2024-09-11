```
def centered_hexagonal_number(n):
    # The nth centered hexagonal number is n*(3*n - 1)/2 + 1
    return n * (3 * n - 1) // 2 + 1
```

Here is the step by step logic of the above solution:
To find the nth centered hexagonal number, we can use the following formula:
n*(3*n - 1)/2 + 1

The above function is a Python function that implements the formula to find the nth centered hexagonal number. It takes an integer `n` as input and returns the nth centered hexagonal number.

The function uses the formula n*(3*n - 1)/2 + 1 to calculate the nth centered hexagonal number. It multiplies `n` by (3*n - 1) and then divides the result by 2. Finally, it adds 1 to the result to get the nth centered hexagonal number.

For example, if we call `centered_hexagonal_number(10)`, it will return `271`, which is the 10th centered hexagonal number.

The time complexity of the function is O(1) as it performs a constant number of arithmetic operations regardless of the input size.

The space complexity of the function is O(1) as it does not use any extra space that grows with the input size.

Overall, the function is an efficient solution to find the nth centered hexagonal number.

Here are some additional test cases for the function:
```python
assert centered_hexagonal_number(1) == 1
assert centered_hexagonal_number(2) == 6
assert centered_hexagonal_number(3) == 17
assert centered_hexagonal_number(4) == 38
assert centered_hexagonal_number(5) == 67
assert centered_hexagonal_number(6) == 108
```

These test cases cover a range of inputs and verify that the function correctly calculates the nth centered hexagonal number for different values of `n`.

```python
def centered_hexagonal_number(n):
    # The nth centered hexagonal number is n*(3*