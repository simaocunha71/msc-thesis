```
def last_Digit_Factorial(n):
    if n == 0 or n == 1:
        return 1
    last_digit = 1
    for i in range(2, n+1):
        last_digit *= i
        last_digit %= 10
    return last_digit
```


The problem is asking to write a function that finds the last digit of the factorial of a given number. For example, the last digit of the factorial of 4 is 4.

The unit test `assert last_Digit_Factorial(4) == 4` helps to understand the problem better.

Here is the Python function that solves the problem:

```
def last_Digit_Factorial(n):
    if n == 0 or n == 1:
        return 1
    last_digit = 1
    for i in range(2, n+1):
        last_digit *= i
        last_digit %= 10
    return last_digit
```

This function works by iterating over the range from 2 to n (inclusive) and multiplying the last_digit by each number in the range. After each multiplication, it takes the last digit of the result by using the modulus operator `%` with 10. The function returns the last_digit, which is the last digit of the factorial of n. If n is 0 or 1, the function returns 1 because the factorial of 0 and 1 is 1. 





Explanation:
The idea is to calculate the factorial of the given number and then find the last digit of the result. 

We start by initializing a variable `last_digit` to 1. Then we iterate over the range from 2 to n (inclusive). For each number in the range, we multiply `last_digit` by that number. After each multiplication, we take the last digit of the result by using the modulus operator `%` with 10. This is because the last digit of a product of numbers is the same as the product of the last digits of those numbers.

Finally, we return the `last_digit`, which is the last digit of the factorial of n.

The time complexity of this function is O(n) because it needs to iterate over the range from 2 to n. The space complexity is O(1) because it only uses a constant amount of space to store the `last_digit` variable.