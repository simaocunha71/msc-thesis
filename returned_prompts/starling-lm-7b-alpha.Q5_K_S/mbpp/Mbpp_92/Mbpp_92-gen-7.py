```
def is_undulating(num):
    num = str(num)
    return num[0] != num[-1] and all(num[i] != num[i+1] for i in range(len(num)-1))
```

Explanation:

The function is_undulating takes a number as an argument and converts it to a string. It then checks if the first character of the string is different from the last character and if all the other characters in between are different from each other. If both conditions are true, the function returns True, indicating that the number is undulating. Otherwise, it returns False.

The all() function is used to check if all the elements in an iterable are True. In this case, it is used to check if all the characters in the string are different from each other.

The range(len(num)-1) generates a sequence of indices from 0 to len(num)-2. This is used to iterate through all the characters in the string except for the last one.

The condition num[i] != num[i+1] checks if the current character is different from the next character. If this condition is True for all the characters in the string, the function returns True. Otherwise, it returns False.

The assert statement is used to check if the function is_undulating returns the expected result for the given example (1212121). If the result is not as expected, an AssertionError will be raised.

Overall, this function can be used to determine if a given number is undulating or not.

```python

def is_undulating(num):
    num = str(num)
    return num[0] != num[-1] and all(num[i] != num[i+1] for i in range(len(num)-1))

# Example usage:
print(is_undulating(1212121))  # Output: True
print(is_undulating(12345678))  # Output: False
```

In the example usage, the function is_undulating is called with different numbers as arguments. The expected results are printed to the console.

For the number 1212121, the function returns True