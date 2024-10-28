"""
The task is to create a Python function that takes a string as input and returns the same string but in uppercase.

The unit test provided, `assert is_upper("person") =="PERSON"`, suggests that the function should return the string in uppercase.

Here is a simple solution using Python's built-in string method `upper()`:

```Python
def is_upper(s):
    return s.upper()
```

This function will take a string `s` as input, convert it to uppercase using the `upper()` method, and return the result. The unit test provided will pass with this solution.

For example, if you call the function with the string `"person"`, it will return `"PERSON"`. """  # NOQA: F401
import unittest

class TestIsUpper(unittest.TestCase):
    def test_is_upper(self):
        self.assertEqual(is_upper("person"), "PERSON")

if __name__ == "__main__":
    unittest.main()  # NOQA: F401

def is_upper(s):
    return s.upper()  # NOQA: F401

print(is_upper("person"))  # Output: PERSON  # NOQA: F401
print(is_upper("hello"))  # Output: HELLO  # NOQA: F401
print(is_upper("world"))  # Output: WORLD  # NOQA: F401
print(is_upper("python"))  # Output: PYTHON  # NOQA: F401
print(is_upper("programming"))  # Output: PROGRAMMING  # NOQA: F401
print(is_upper("exercise"))  # Output: EXERCISE  # NOQA: F401
print(is_upper("testing"))  # Output: TESTING  # NOQA: F401
print(is_upper("conversion"))  # Output: CONVERSION  # NOQA: F401
print(is_upper("function"))  # Output: FUNCTION  # NOQA: F401
print(is_upper("convert"))  # Output: CONVERT  # NOQA: F401
print(is_upper("string"))  # Output: STRING  # NOQA: F401
print(is_upper("to"))  # Output: TO  # NOQA: F401
print(is_upper("uppercase"))  # Output: UPPERCASE  # NOQA: F401
print(is_upper("python"))  # Output: PYTHON  # NOQA: F401
print(is_upper("programming"))  # Output: PROGRAMMING  # NOQA: F401
print