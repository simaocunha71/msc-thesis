```
def text_match_wordz(text):
    return 'z' in text
```
This function takes a string as input and checks if the string contains the character 'z'. If it does, the function returns True; otherwise, it returns False. The unit test `assert text_match_wordz("pythonz.")==True` ensures that the function works correctly. 

For example, if you call `text_match_wordz("pythonz.")`, the function will return True because the string "pythonz." contains the character 'z'. If you call `text_match_wordz("hello")`, the function will return False because the string "hello" does not contain the character 'z'. 