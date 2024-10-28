```
def text_match_wordz(text):
    return 'z' in text
```
The problem is asking you to write a function that checks if a given text contains the letter 'z'. 

The unit test `assert text_match_wordz("pythonz.")==True` suggests that the function should return `True` if the text contains 'z' and `False` otherwise.

The function `text_match_wordz` can be implemented by using the `in` operator in Python, which checks if a substring is present in a given string. If 'z' is present in the text, the function returns `True`; otherwise, it returns `False`.  This solution is straightforward and efficient, as it only requires a single operation to check for the presence of 'z' in the text.  Therefore, the provided solution is correct and passes the given unit test. 