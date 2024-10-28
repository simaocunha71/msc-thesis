The problem is asking you to create a function that checks if a given text contains the word 'z'. The function should return True if 'z' is found and False otherwise.

The unit test `assert text_match_wordz("pythonz.")==True` suggests that the function should check if the word 'z' is present in the given text.

Here's a Python function that solves the problem:

```python
def text_match_wordz(text):
    return 'z' in text
```

This function uses the `in` operator to check if the string 'z' is present in the given text. If 'z' is found, the function returns True; otherwise, it returns False. The unit test `assert text_match_wordz("pythonz.")==True` will pass with this function. 