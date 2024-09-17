The problem is asking to create a function that checks if a given string contains the character 'z' in the middle of the string, excluding the start and end of the word.

However, the problem description does not specify whether the function should return a boolean value or not. But, thanks to the unit test provided, `assert text_match_wordz_middle("pythonzabc.")==True`, we can infer that the function should return `True` if 'z' is present in the middle of the string and `False` otherwise.

Here is the solution:
```python
def text_match_wordz_middle(text):
    return 'z' in text[1:-1]
```
This function uses Python's string slicing feature to exclude the first and last characters of the string. The `in` operator is then used to check if 'z' is present in the resulting substring. If 'z' is found, the function returns `True`; otherwise, it returns `False`.