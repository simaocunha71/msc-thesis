```
def text_match_wordz_middle(text):
    if len(text) < 3:
        return False
    return text[1:-1].find('z') != -1
```


The function `text_match_wordz_middle` checks if a given string `text` contains 'z' except at the start and end of the word. It first checks if the length of the string is less than 3 (to avoid index out of range error), then it checks if the string `text[1:-1]` (all characters except the first and last) contains 'z' using the `find` method. If 'z' is found, it returns `True`, otherwise it returns `False`. The unit test `assert text_match_wordz_middle("pythonzabc.")==True` ensures the function works correctly. 





