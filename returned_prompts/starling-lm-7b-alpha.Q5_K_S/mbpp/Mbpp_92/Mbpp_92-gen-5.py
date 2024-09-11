```
def is_undulating(num):
    num = str(num)
    for i in range(len(num)-1):
        if num[i] != num[i+1]:
            return True
    return False
```

In this code, the function `is_undulating` takes a number as an argument and converts it to a string. It then iterates through the string, comparing each character with the next character. If the characters are not equal, the function returns True, indicating that the number is undulating. If the characters are equal for all iterations, the function returns False, indicating that the number is not undulating.

To test this function, you can use the `assert` statement to check if the function correctly identifies the given number as undulating (in this case, the number 1212121). The `assert` statement will raise an error if the expected result is not equal to the actual result, helping you catch any potential bugs in your code.

Overall, this function provides a simple and efficient way to determine whether a given number is undulating or not.

```python
def is_undulating(num):
    num = str(num)
    for i in range(len(num)-1):
        if num[i] != num[i+1]:
            return True
    return False

# Testing the function
assert is_undulating(1212121) == True
```

This code defines the `is_undulating` function, which takes a number as an argument and checks if it is undulating. The function converts the number to a string and then iterates through the string, comparing each character with the next character. If the characters are not equal, the function returns True. If all characters are equal, the function returns False.

To test the function, an `assert` statement is used. The `assert` statement checks if the result of the function (in this case, the result of `is_undulating(1212121)`) is equal to the expected result (True). If the result is not equal to the expected result, an error will be raised.

In this specific case, the `assert` statement is used to verify that the function correctly identifies the number 1212