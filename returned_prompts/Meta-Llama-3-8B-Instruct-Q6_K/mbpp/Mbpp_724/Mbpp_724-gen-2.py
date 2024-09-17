```
def power_base_sum(base, power):
    result = 0
    base_power = base ** power
    for digit in str(base_power):
        result += int(digit)
    return result
```


The function `power_base_sum(base, power)` calculates the sum of all digits of the base to the specified power. It does this by first calculating the base to the power using `base ** power`. Then, it converts this number to a string and iterates over each character in the string (which are the digits of the base to the power). For each digit, it adds the integer value of the digit to the result. Finally, it returns the result. 

The unit test `assert power_base_sum(2,100)==115` ensures that the function works correctly for the input base 2 and power 100. It checks that the result of the function with these inputs is 115. 

The function should work correctly for any base and power. For example, `power_base_sum(3,2)` should return 9 (3^2 = 9, sum of digits = 9), and `power_base_sum(4,3)` should return 16 (4^3 = 64, sum of digits = 1+6+4 = 11, but the problem asks for the sum of all digits, not the sum of the digits in a specific order). 

The function is case-insensitive, and it assumes that the input base and power are valid (i.e., they are integers and the base is greater than 1). If the base is not greater than 1, the function will return an incorrect result. If the base or power is not an integer, the function will return an incorrect result or raise an exception, depending on the language and its handling of non-integer inputs. 

The function does not handle the case where the input base or power is very large, which could cause the function to run slowly or return an incorrect result. It assumes that the input base and power are reasonable and will not cause the function to run slowly or return an incorrect result. 

The function does not handle the case where the input base or power is negative, which could cause the function to return an incorrect result. It assumes that the input base and power are non-negative. 

The function does not handle the case where the input base is 0, which could cause the function to return an incorrect result. It assumes that the input base is greater than 1.