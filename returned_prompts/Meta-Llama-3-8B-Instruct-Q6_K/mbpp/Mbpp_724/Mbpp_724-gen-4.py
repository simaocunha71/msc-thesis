```
def power_base_sum(base, power):
    result = 1
    for _ in range(power):
        result *= base
    return sum(int(digit) for digit in str(result))
```



The problem is asking you to write a function that calculates the sum of all digits of a number that is the result of a base raised to a power. 

The unit test `assert power_base_sum(2,100)==115` suggests that the function should return 115 when the base is 2 and the power is 100.

Here is a Python solution for this problem. It starts by initializing a variable `result` to 1. Then it raises the base to the power using a loop. After that, it converts the result to a string, iterates over each character in the string (which are the digits of the result), converts each character back to an integer, and sums them up.

Here is the solution:
```
def power_base_sum(base, power):
    result = 1
    for _ in range(power):
        result *= base
    return sum(int(digit) for digit in str(result))
```



This function works by first calculating the base to the power using a loop. Then it converts the result to a string and sums up the digits. The unit test `assert power_base_sum(2,100)==115` passes, which means the function is working correctly. 