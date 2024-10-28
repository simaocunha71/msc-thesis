```
def last_Digit_Factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res % 10
```


Explanation:
The function takes an integer n as input and calculates the factorial of n. The factorial is then reduced to its last digit by using the modulus operator `%`. The last digit is then returned. For example, if the input is 4, the function will calculate 4! = 24, which is 4 when reduced to its last digit. The unit test `assert last_Digit_Factorial(4) == 4` ensures this result. 

This function works by iterating over the range from 1 to n (inclusive) and multiplying each number to the result. The result is then reduced to its last digit by using the modulus operator `%`. This approach has a time complexity of O(n) as it needs to iterate over the range from 1 to n. 

Note: The unit test `assert last_Digit_Factorial(4) == 4` ensures that the function returns the correct last digit of the factorial for the input 4. This test can be extended to other inputs to ensure the function works correctly for all positive integers. 





```
```python
def last_Digit_Factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res % 10
```


Explanation:
The function takes an integer n as input and calculates the factorial of n. The factorial is then reduced to its last digit by using the modulus operator `%`. The last digit is then returned. For example, if the input is 4, the function will calculate 4! = 24, which is 4 when reduced to its last digit. The unit test `assert last_Digit_Factorial(4) == 4` ensures this result. 

This function works by iterating over the range from 1 to n (inclusive) and multiplying each number to the result. The result is then reduced to its last digit by using the modulus operator `%`. This approach has a time complexity of O(n) as it needs to iterate over the range from 1 to n. 

Note: The unit test `assert last_Digit_Factorial(4) == 4` ensures that the function returns the correct last digit of the factorial for the input 4. This test can be extended to