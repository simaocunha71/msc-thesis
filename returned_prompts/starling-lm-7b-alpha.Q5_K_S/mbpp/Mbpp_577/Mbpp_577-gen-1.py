from math import factorial

def last_Digit_Factorial(n):
    return factorial(n) % 10


# Test the function
print(last_Digit_Factorial(4) == 4)


"""
In this function, we are using the Python built-in math module to calculate factorial of a number. We then return the last digit of the factorial by taking modulo 10.
The assert statement is used to test the function. The expected result is 4, which is the last digit of the factorial of 4.
"""

```
```

# Python3 program to find the last digit in
# factorial of a given number

# Function to find the last digit in factorial of a given number
def last_Digit_Factorial(n):
    # Calculating factorial of n
    fact = factorial(n)

    # Returning last digit of factorial
    return fact % 10

# Driver Code
if __name__ == "__main__":
    n = 4
    print(last_Digit_Factorial(n))
```
```

The Python3 program to find the last digit in factorial of a given number is as follows:

```python
# Python3 program to find the last digit in
# factorial of a given number

# Function to find the last digit in factorial of a given number
def last_Digit_Factorial(n):
    # Calculating factorial of n
    fact = factorial(n)

    # Returning last digit of factorial
    return fact % 10

# Driver Code
if __name__ == "__main__":
    n = 4
    print(last_Digit_Factorial(n))
```

This program defines a function `last_Digit_Factorial(n)` that calculates the factorial of a number `n` using the `factorial()` function from the `math` module. It then returns the last digit of the factorial by taking the modulo 10.

In the driver code, we set `n` to 4 and print the result of `last_Digit_Factorial(n)