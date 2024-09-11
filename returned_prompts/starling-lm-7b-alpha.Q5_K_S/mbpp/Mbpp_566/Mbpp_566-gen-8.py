```
def sum_digits(num):
    sum = 0
    while num:
        sum += num % 10
        num //= 10
    return sum
```

Explanation:
This function uses a while loop to repeatedly subtract the last digit of the number until the number becomes 0.
During each iteration, the function adds the last digit of the number to the sum and then removes the last digit by taking the modulus of the number with 10 and then performing an integer division by 10.

For example, when sum_digits(345) is called, the function performs the following steps:

- In the first iteration, the function adds 5 to the sum and then sets num to 34.
- In the second iteration, the function adds 4 to the sum and then sets num to 3.
- In the third iteration, the function adds 3 to the sum and then sets num to 0. Since num is now 0, the loop ends.
- The function returns the sum, which is 12.

The function correctly calculates the sum of the digits of the given number and satisfies the requirement of the problem.

In addition to the correct implementation, the function also demonstrates the use of the modulus and integer division operations in Python.

The modulus operation (%) returns the remainder of the division of the first operand by the second operand. For example, 34 % 10 is equal to 4, as 34 divided by 10 leaves a remainder of 4.

The integer division operation (//) performs an integer division, which means that it ignores the remainder. For example, 34 // 10 is equal to 3, as 34 divided by 10 is 3 with no remainder.

These operations are commonly used in programming to extract the last digit of a number or to remove the last digit of a number.

Overall, this function provides a simple and efficient solution to the problem of calculating the sum of the digits of a non-negative integer.

"""
```

python

```python
def sum_digits(num):
    sum = 0
    while num:
        sum += num % 10
        num