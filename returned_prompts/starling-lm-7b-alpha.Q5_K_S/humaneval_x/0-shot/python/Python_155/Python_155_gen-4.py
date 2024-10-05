
To solve this problem, you can follow these steps:

1. Convert the input integer to a string, so that you can iterate through each digit.
2. Initialize two counters for even and odd digits to zero.
3. Iterate through each character in the string.
4. Check if the character is an even number (i.e., '0', '2', '4', '6', '8'). If it is, increment the even counter by 1. Otherwise, increment the odd counter by 1.
5. Return the result as a tuple of the form (even, odd).

Here's a Python implementation of the function:

```python
def even_odd_count(num):
    num_str = str(abs(num))  # Convert the input integer to a string
    even_count = 0
    odd_count = 0

    for digit in num_str:
        if int(digit) % 2 == 0:  # Check if the digit is even
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)
```

You can test the function with the provided examples:

```python
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)
```

The function correctly calculates and returns the number of even and odd digits in the given integers.

In the provided code, the function `even_odd_count` takes an integer as input and converts it to a string using the `str` function. It initializes two counters, `even_count` and `odd_count`, to keep track of the number of even and odd digits, respectively. 

The function then iterates through each character in the string representation of the input integer. For each digit, it checks if it is even (i.e., divisible by 2) using the modulo operator `%`. If the digit is even, it increments the `even_count` counter by 1; otherwise, it increments the `odd_count` counter by 1. 

Finally,