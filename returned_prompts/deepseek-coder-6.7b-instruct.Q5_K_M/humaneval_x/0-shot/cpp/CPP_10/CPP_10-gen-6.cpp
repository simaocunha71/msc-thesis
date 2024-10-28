Here is a Python solution:

```python
def is_palindrome(s):
    return s == s[::-1]

def make_palindrome(s):
    if is_palindrome(s):
        return s
    for i in range(len(s)):
        if is_palindrome(s[i:]):
            return s + s[:i][::-1]

print(make_palindrome(""))  # ""
print(make_palindrome("cat"))  # "catac"
print(make_palindrome("cata"))  # "catac"
```

In this Python function, we first check if the input string is a palindrome. If it is, we return the string as it is. If it isn't,