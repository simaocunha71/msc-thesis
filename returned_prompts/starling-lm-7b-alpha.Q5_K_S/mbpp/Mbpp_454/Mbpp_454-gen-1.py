```
def text_match_wordz(text):
    if 'z' in text:
        return True
    else:
        return False
```

# Python3 Program

```python
def text_match_wordz(text):
    if 'z' in text:
        return True
    else:
        return False
```

The above Python program defines a function `text_match_wordz(text)` which takes a string as an argument and checks if the string contains the letter 'z'. The function returns `True` if the letter 'z' is found in the string, otherwise it returns `False`.

To verify the function, the following assertion is provided:

```python
assert text_match_wordz("pythonz.")==True
```

This assertion checks if the function `text_match_wordz("pythonz.")` returns `True` as expected. If the function returns `True` for the given string, the assertion passes and the program executes successfully. Otherwise, if the function returns `False`, an AssertionError is raised and the program execution is aborted. 

This assertion serves as a test case to ensure the correctness of the `text_match_wordz` function for strings containing the letter 'z'. 

In the provided Python program, the `assert` keyword is used to define the assertion. The `assert` keyword in Python is used to check if a condition is true. If the condition is false, an AssertionError is raised, indicating that the condition should never be false. 

The `==` operator is used to compare the result of the `text_match_wordz` function with the expected value, `True`. If the result matches the expected value, the assertion passes. 

Overall, this Python program defines a function that checks if a given string contains the letter 'z' and provides a test case to verify the correctness of the function.
```
```

In the provided Python program, the function `text_match_wordz(text)` is defined to take a string `text` as an argument. The function checks if the letter 'z' is present in the given string `text`. If 'z' is found in the string, the function returns `True`; otherwise,