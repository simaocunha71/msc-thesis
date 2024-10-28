```
def text_match_wordz_middle(text):
    if len(text)<3:
        return False
    return 'z' in text[1:-1]
```





The problem asks for a function that checks if a given string contains the character 'z' except at the start and end of the word. 

However, the problem statement is not clear about whether the function should return a boolean value indicating whether the condition is met or not, or it should return the index of the 'z' character in the string.

Thanks to the unit test provided, `assert text_match_wordz_middle("pythonzabc.")==True`, it can be inferred that the function should return a boolean value indicating whether the condition is met or not.

Here's a Python solution for the problem:

The function `text_match_wordz_middle` checks if the length of the input string is less than 3. If it is, the function returns `False` because a string of length less than 3 cannot contain 'z' in the middle.

If the length of the string is 3 or more, the function checks if 'z' is in the string excluding the first and last characters. This is done using string slicing with `text[1:-1]`. If 'z' is found in this slice, the function returns `True`; otherwise, it returns `False`.