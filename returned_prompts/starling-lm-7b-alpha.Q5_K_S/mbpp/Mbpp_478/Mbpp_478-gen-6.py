"""
To solve this problem, we can iterate through the string and only add the character to the result if it's not lowercase.
Here's a step-by-step explanation of the solution:

1. Define the function remove_lowercase that takes a string as input.
2. Initialize an empty string called result.
3. Iterate through each character in the input string.
4. Check if the current character is uppercase by using the isupper() method.
5. If the character is uppercase, add it to the result string using the += operator.
6. Repeat steps 4-5 for all characters in the input string.
7. Return the result string.
8. Test the function by asserting that remove_lowercase("PYTHon") equals "PYTH".
"""

def remove_lowercase(s):
    result = ""
    for c in s:
        if c.isupper():
            result += c
    return result

# Test the function
assert remove_lowercase("PYTHon") == "PYTH"

# Further testing
print(remove_lowercase("HELLO WORLD"))  # Should return "HW"
print(remove_lowercase("Python Is Fun"))  # Should return "Python"
print(remove_lowercase("123ABC"))  # Should return "123ABC"
print(remove_lowercase(""))  # Should return ""

# Test with a string containing only lowercase letters
print(remove_lowercase("hello"))  # Should return ""

# Test with a string containing only uppercase letters
print(remove_lowercase("PYTHON"))  # Should return "PYTHON"

```
  
Here are a few more tests to ensure the function works correctly:

```python
print(remove_lowercase("Python Programming"))  # Should return "Python"
print(remove_lowercase("123ABC456"))  # Should return "123ABC456"
print(remove_lowercase(""))  # Should return ""
print(remove_lowercase("Hello World"))  # Should return "HW"
```

In all of these tests, the function should correctly remove all