Here is the Python code for the problem:

```Python
def countNums(arr):
    return sum(1 for num in arr if sum(int(digit) for digit in str(abs(num))) > 0)
```

Explanation:
The problem is asking to count the numbers in the given array which have a sum of digits greater than 0. If a number is negative, its first signed digit will be negative. We use Python's built-in `sum` function and a generator expression to achieve this.

Here's a step-by-step breakdown:

1. `for num in arr`: This loops over each number in the array.
2. `str(abs(num))`: This converts the absolute value of each number to a string. This is done to easily iterate over each digit of the number.
3. `int(digit) for digit in str(abs(num))`: This converts each character (digit) in the string back to an integer.
4. `sum(int(digit) for digit in str(abs(num))) > 0`: This calculates the sum of the digits of the number and checks if it's greater than 0.
5. `sum(1 for ... )`: This counts the number of numbers in the array that satisfy the condition (i.e., have a sum of digits greater than 0).

The `abs` function is used to ensure that the sum of digits is calculated correctly for negative numbers. For example, for the number -123, `abs(-123)` would be 123, and the sum of its digits would be 6. The `str` function is used to convert the number to a string, which allows us to easily iterate over each digit. The `int` function is used to convert each character (digit) back to an integer, and the `sum` function is used to calculate the sum of the digits. The `if` statement checks if the sum of the digits is greater than 0, and the `sum` function at the end counts the number of numbers that satisfy this condition.