"""
The above problem can be solved using the `replace()` function in Python. The `replace()` function returns a copy of the original string with all occurrences of a substring replaced by another substring. Here, we can use `' '` as the substring to be replaced and an empty string `''` as the replacement substring.

Here's a step-by-step walkthrough on how you can do this:

- Define a function called `remove_whitespaces` that takes a string as an input.
- Inside the function, use the `replace()` function to replace all whitespaces (`' '`) with an empty string (`''`). This will remove all whitespaces from the string.
- Return the modified string from the function.

Here's the Python code that implements the above algorithm:
"""
def remove_whitespaces(string):
    return string.replace(" ", "")

# Test the function
print(remove_whitespaces(' Google    Flutter '))  # Output: GoogleFlutter

```python
```

In the above code, the `remove_whitespaces` function takes a string as an input and returns the modified string with all whitespaces removed. The `replace()` function is used to replace all occurrences of whitespaces with an empty string. The modified string is then returned from the function.

The provided test case `remove_whitespaces(' Google    Flutter ')` returns `'GoogleFlutter'` as expected.

Note: The `replace()` function in Python is case-sensitive, so it only replaces uppercase whitespaces with uppercase letters, and lowercase whitespaces with lowercase letters. If you want to replace whitespaces regardless of their case, you can use a regular expression pattern in the `replace()` function like this: `'\\s+'`. Here's how you can modify the `remove_whitespaces` function to handle this:

```python
def remove_whitespaces(string):
    return string.replace('\\s+', '')
```

With this modification, the `remove_whitespaces` function will remove all whitespaces from the string, regardless of their case.

```python
print(remove_whitespaces(' Google    Flutter ')) 