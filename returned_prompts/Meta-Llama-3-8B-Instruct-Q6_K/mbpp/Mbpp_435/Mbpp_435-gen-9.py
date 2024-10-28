```
def last_Digit(n):
    return n % 10
```





Python function to find the last digit of a given number. The function works by using the modulus operator `%` which returns the remainder of the division of the number by 10. This remainder is the last digit of the number. For example, if the input number is 123, the function will return 3 which is the last digit of the number 123.

The unit test `assert last_Digit(123) == 3` confirms that the function works correctly. It checks if the last digit of the number 123 is 3, which it should be, and if the function returns 3, which it does. Therefore, the function passes the unit test.