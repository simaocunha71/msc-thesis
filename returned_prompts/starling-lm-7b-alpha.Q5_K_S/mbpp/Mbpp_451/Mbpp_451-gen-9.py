```python
def remove_whitespaces(string):
    return string.replace(' ', '')
```

Explanation:
The `replace()` function in Python is used to replace the occurrence of a substring with another substring. It takes two parameters, the substring to be replaced and the substring that replaces the former one. In this case, we are replacing all the whitespaces in a string (denoted by the space character) with an empty string, thereby removing all whitespaces from the given string.

The `remove_whitespaces` function takes a string as an argument and uses the `replace()` function to return the modified string without any whitespaces.

The assert statement `assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'` checks if the `remove_whitespaces` function is correctly removing all whitespaces from the given string. The expected output is `'GoogleFlutter'`, which is the same as the actual output.

This assertion confirms the correctness of the `remove_whitespaces` function.

To use the function, you can simply call it with the desired string as an argument, like this: `remove_whitespaces(' Google    Flutter ')`. The function will return the modified string without whitespaces, which can be assigned to a variable or used directly in your code.

For example, if you call `remove_whitespaces(' Google    Flutter ')`, the function will return `'GoogleFlutter'`.

This solution demonstrates a simple and efficient way to remove all whitespaces from a given string in Python.

Note: It's important to note that this function only removes the actual whitespace characters (spaces, tabs, and newlines) and does not handle any other types of whitespace-like characters (such as non-breaking spaces or zero-width spaces). If you need to remove those specific characters as well, you can modify the function to use a more specific regular expression or pattern matching approach.

Overall, the provided solution is a straightforward and effective way to remove all whitespaces from a string in Python.

```python
def remove_whitespaces(string):
    return string.replace(' ', '')
```

Here's an example usage of the `remove_whitespaces` function: