def toggle_string(s):
    return ''.join(chr(256 - ord(c)) if c.isalpha() else c for c in s)


def test_toggle_string():
    assert toggle_string("Python") == "pYTHON"
    print("Passed")


test_toggle_string()


"""
The provided code defines a function toggle_string that takes in a string and returns a new string with the case of all characters toggled. The function uses a generator expression and the join method to iterate over each character in the input string. If a character is alphabetic, it is replaced with its complementary character (i.e., uppercase becomes lowercase and vice versa). If a character is not alphabetic, it is left unchanged. The resulting list of characters is then joined into a single string using the join method and returned as the output. The code also includes a test_toggle_string function that checks if the toggle_string function correctly toggles the case of all characters in the input string "Python". If the test passes, the message "Passed" is printed.
"""

```python
# Toggle a string's characters
def toggle_string(s):
    return ''.join(chr(256 - ord(c)) if c.isalpha() else c for c in s)

def test_toggle_string():
    assert toggle_string("Python") == "pYTHON"
    print("Passed")

test_toggle_string()
```

This program defines a function `toggle_string` that takes in a string and returns a new string with the case of all characters toggled. The function uses a generator expression and the `join` method to iterate over each character in the input string. If a character is alphabetic, it is replaced with its complementary character (i.e., uppercase becomes lowercase and vice versa). If a character is not alphabetic, it is left unchanged. The resulting list of characters is then joined into a single string using the `join` method and returned as the output.

The program also includes a `test_toggle_string` function that checks if the `toggle_string` function correctly toggles the case of all characters in the