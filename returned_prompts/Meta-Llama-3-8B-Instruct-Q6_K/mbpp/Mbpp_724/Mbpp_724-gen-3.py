```
def power_base_sum(base, power):
    result = 0
    for digit in str(base ** power):
        result += int(digit)
    return result
``` 

The problem asks to write a function that takes a base and a power as arguments and calculates the sum of all digits of the base raised to the power. For example, if the base is 2 and the power is 100, the function should calculate the sum of all digits of 2^100. 

The unit test `assert power_base_sum(2,100)==115` helps to understand the problem better. It means that the function should return 115 when the base is 2 and the power is 100.

The solution uses a loop to iterate over each digit of the result of the base raised to the power. It converts the result to a string and then iterates over each character (digit) in the string, adding it to the result. Finally, it returns the result. 

This solution assumes that the power is a positive integer. If the power can be negative or a non-integer, additional error checking would be needed. 

For example, the function would need to handle the case where the base is 0 and the power is negative, or where the power is a non-integer. In such cases, the function could raise an error or return a special value to indicate an invalid input. 

In this solution, the function does not handle these cases. It simply calculates the sum of the digits of the base raised to the power, assuming that the input is valid. If the input is invalid, the function may produce incorrect results or raise an error. 

To make the function more robust, you could add error checking to handle invalid inputs. For example, you could check that the power is a positive integer, and raise an error if it is not. You could also check that the base is a positive integer, and raise an error if it is not. 

Here is the modified function with error checking:
```
def power_base_sum(base, power):
    if not isinstance(base, int) or base <= 0:
        raise ValueError("Base must be a positive integer")
    if not isinstance(power, int) or power < 0:
        raise ValueError("Power must be a non-negative integer")
    result = 0
    for digit in str(base ** power):
        result += int(digit)
    return result
``` 
This function raises a ValueError if the base is not a positive