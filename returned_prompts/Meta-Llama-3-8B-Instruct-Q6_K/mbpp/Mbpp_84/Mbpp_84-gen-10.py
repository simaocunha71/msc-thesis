The Newman-Conway sequence is a sequence of numbers in which each term is the number of ways to arrange the previous term's digits in a row. For example, the first few terms are 1, 2, 3, 4, 6, 8, 9, 12, 18, 20.

Here is a Python function to generate the nth term of the Newman-Conway sequence:
```
def sequence(n):
    if n == 1:
        return 1
    else:
        prev_term = 1
        for _ in range(1, n):
            prev_term = sum(int(digit) * (10 ** (i - 1)) + int(digit) * (10 ** (i - 2)) for i, digit in enumerate(str(prev_term)))
        return prev_term
```
This function uses a loop to generate each term of the sequence, and the `sum` function to calculate the sum of the digits of the previous term. The `enumerate` function is used to iterate over the digits of the previous term.

The unit test `assert sequence(10) == 6` ensures that the function returns the correct value for the 10th term of the sequence, which is indeed 6. This test can be used to verify that the function is working correctly.