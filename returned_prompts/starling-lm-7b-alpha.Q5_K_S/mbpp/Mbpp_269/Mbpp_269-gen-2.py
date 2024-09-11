
```python
def ascii_value(c):
    return ord(c)
```

This function `ascii_value` takes a character as an input and uses the built-in `ord()` function to return the ASCII value of the character. The `ord()` function takes a single character as an argument and returns its corresponding Unicode code point. In ASCII, the first 128 characters have the same code points, so the ASCII value of 'A' is indeed 65.

To use the function, simply pass the character you want to find the ASCII value of as an argument. For example, `ascii_value('A')` will return 65, and `ascii_value('z')` will return 122.

Here's an example of how to use the function:

```python
print(ascii_value('A'))  # Output: 65
print(ascii_value('z'))  # Output: 122
```

The `print()` function is used to display the result of the function call. In this case, it will print the ASCII values of the characters 'A' and 'z' to the console.

I hope this helps! Let me know if