The problem is asking to create a function that determines whether a given number is undulating or not. An undulating number is a number that has an alternating pattern of digits, where each digit is either 0 or 1.

The unit test `assert is_undulating(1212121) == True` helps to understand the problem better. It shows that the number 1212121 is indeed an undulating number because it has an alternating pattern of digits.

Here's a Python function that solves the problem:
```
def is_undulating(n):
    s = str(n)
    for i in range(1, len(s)):
        if (s[i-1] == s[i]):
            return False
    return True
```
This function converts the given number to a string and then checks each pair of adjacent digits. If it finds any pair with the same digit, it returns False, indicating that the number is not undulating. If it doesn't find any such pair, it returns True, indicating that the number is undulating.