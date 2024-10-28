The problem is asking to create a function that checks if a given string contains the character 'z' anywhere in the middle of the string, excluding the start and end of the word.

The provided unit test `assert text_match_wordz_middle("pythonzabc.")==True` suggests that the function should return `True` if 'z' is found in the middle of the string, and `False` otherwise.

Here's a Python function that solves the problem:
```
def text_match_wordz_middle(text):
    return 'z' in text[1:-1]
```
This function uses Python's string slicing feature to exclude the start and end of the string, and then checks if the character 'z' is present in the resulting substring using the `in` operator. If 'z' is found, the function returns `True`, otherwise it returns `False`.