
Here's the solution:

```
def count_nums(arr):
    return sum(1 for num in arr if sum(int(digit) for digit in str(abs(num))) > 0)
```

Explanation:

*   We use a generator expression inside the built-in `sum` function to count the number of elements in the array that have a sum of digits greater than 0.
*   The `abs` function is used to convert negative numbers to positive, so that the sum of digits is calculated correctly.
*   The `str` function is used to convert the number to a string, and the `int` function is used to convert each character (digit) in the string to an integer.
*   The `sum` function is used to calculate the sum of the digits.
*   The `if` condition checks if the sum of the digits is greater than 0, and if true, adds 1 to the count.
*   The `sum` function returns the total count of elements