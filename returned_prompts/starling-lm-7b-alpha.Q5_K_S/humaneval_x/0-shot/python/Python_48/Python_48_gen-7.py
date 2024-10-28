
Here's a simple function that checks if a given string is a palindrome:

```python
def is_palindrome(text: str):
    # Removing all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum())

    # Checking if the string is a palindrome
    return text == text[::-1]
```

This function first removes all non-alphanumeric characters from the input string, then checks if the resulting string is the same when reversed. If the two strings are the same, the function returns True, indicating that the input string is a palindrome; otherwise, it returns False.

You can use the `is_palindrome` function like this:

```python
print(is_palindrome(''))  # Output: True
print(is_palindrome('aba'))  # Output: True
print(is_palindrome('aaaaa'))  # Output: True
print(is_palindrome('zbcd'))  # Output: False
```

Note that the function is case-sensitive and doesn't ignore spaces or punctuation marks. If you want to ignore case or remove spaces and punctuation, you can modify the function accordingly.

For example, to ignore case and remove spaces and punctuation, you can update the function like this:

```python
def is_palindrome(text: str):
    # Removing all non-alphanumeric characters and converting to lowercase
    text = ''.join(c.lower() for c in text if c.isalnum())

    # Checking if the string is a palindrome
    return text == text[::-1]
```

Here's how you can use the modified function:

```python
print(is_palindrome(''))  # Output: True
print(is_palindrome('aba'))  # Output: True
print(is_palindrome('aaaaa'))  # Output: True
print(is_palindrome('zbcd'))  # Output: True
```

In this version of the function, all non-alphanumeric characters are removed, and the resulting string is converted to lower