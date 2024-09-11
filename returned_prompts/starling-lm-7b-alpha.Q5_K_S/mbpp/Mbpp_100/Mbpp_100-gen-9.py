```
def next_smallest_palindrome(n):
    if not isinstance(n, int):
        raise TypeError("Input is not an integer")
    if n < 10:
        return n + 1
    s = str(n)
    for i in range(len(s)):
        if s[i] != '9':
            break
    if i == len(s) - 1:
        return str(int(s[:i]) + 1 + '0' * (len(s) - i - 1))
    else:
        return str(int(s[:i] + chr(ord(s[i]) + 1) + '9' * (len(s) - i - 1)))
```

The above function first checks if the input is an integer, if not, it will raise a TypeError. Then it converts the input integer to a string, and starts from the back of the string to check if the character is '9'. If the character is '9', it will keep moving to the left until it finds a character that is not '9'. If it reaches the end of the string, it means the next smallest palindrome will be the next number with a '0' at the end (e.g. 99 -> 101). If it finds a character that is not '9', it means it can increment that character and set the remaining characters to '9' (e.g. 199 -> 202).

This function has a time complexity of O(logn), where n is the input number.

It's important to note that this function only works for positive integers less than 10^18.

To test the function, you can use the following code:
```python
print(next_smallest_palindrome(99))  # Output: 101
```

This will print the next smallest palindrome of 99, which is 101.

You can also test other cases, such as:
```python
print(next_smallest_palindrome(123))  # Output: 121
print(next_smallest_palindrome(12345)) 