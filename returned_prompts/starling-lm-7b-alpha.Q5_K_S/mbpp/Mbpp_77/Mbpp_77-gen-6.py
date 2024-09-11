def is_Divisible_By_11(num):
    num_str = str(num)
    if len(num_str) % 2 == 0:
        for i in range(len(num_str) // 2):
            if int(num_str[i]) + int(num_str[len(num_str) - 1 - i]) != 0:
                return False
    else:
        for i in range(len(num_str) // 2):
            if int(num_str[i]) + int(num_str[len(num_str) - 1 - i]) != 0:
                return False
        if int(num_str[len(num_str) // 2]) != 0:
            return False
    return True

assert is_Divisible_By_11(12345) == False











"""
Here is a simple solution to the problem:

To determine if a number is divisible by 11, we need to check if the difference between the sum of its even-positioned digits and the sum of its odd-positioned digits is zero. We can do this by converting the number to a string, and then comparing the sums of the even- and odd-positioned digits.

Here's an example Python function that uses this approach:

```python
def is_Divisible_By_11(num):
    num_str = str(num)
    if len(num_str) % 2 == 0:  # If the number of digits is even
        for i in range(len(num_str) // 2):
            if int(num_str[i]) + int(num_str[len(num_str) - 1 - i]) != 0:  # Check if the sum of the even- and odd-positioned digits is zero
                return False
    else:  # If the number of digits is odd
        for i in range(len(num_str) // 2):
            if int(num_str[i]) + int(num_str[len(num_str) - 1 - i