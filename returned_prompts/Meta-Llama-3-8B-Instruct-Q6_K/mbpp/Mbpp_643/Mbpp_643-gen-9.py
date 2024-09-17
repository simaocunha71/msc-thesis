```
def text_match_wordz_middle(text):
    return 'z' in text[1:-1]
```



The problem is asking to create a function that checks if the character 'z' is present in a given string, but only if it's not at the start or end of the string. 

The unit test `assert text_match_wordz_middle("pythonzabc.")==True` helps to clarify this requirement. It means that if the 'z' is present in the middle of the string, the function should return True.

Here's the Python function to solve this problem:
```
def text_match_wordz_middle(text):
    return 'z' in text[1:-1]
```
This function uses Python's string slicing feature to get the middle part of the string (everything except the first and last characters), and then checks if 'z' is present in that part. If it is, the function returns True; otherwise, it returns False.