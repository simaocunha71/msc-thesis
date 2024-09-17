```
def is_Even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```


Explanation:
This function takes an integer as input and checks whether it is even or not. The condition n % 2 == 0 is used to check if the number is even or not. If the remainder of the number divided by 2 is 0, then the number is even. The function returns True if the number is even and False otherwise. The unit test provided, `assert is_Even(1) == False`, ensures that the function works correctly for odd numbers. 

This function uses the modulo operator `%` to find the remainder of the division of the number by 2. If the remainder is 0, then the number is even, and the function returns `True`. Otherwise, the function returns `False`. This approach is simple and efficient, as it does not require any complex calculations or operations. It is also easy to understand and maintain, making it a good choice for this task. 

The unit test provided ensures that the function works correctly for odd numbers, which is important because the function is designed to check whether a number is even or not. If the function did not work correctly for odd numbers, it would not be a reliable solution. The unit test helps to ensure that the function works correctly in all cases, making it a valuable tool for testing and verifying the function's behavior. 