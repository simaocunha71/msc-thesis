You can solve this problem by using Python's built-in string methods. Here is the solution:
```
def text_match_wordz_middle(text):
    return 'z' in text[1:-1]
```
This function works by slicing the input string to get the middle part (everything except the first and last characters), and then checking if 'z' is in that part. If 'z' is found, the function returns True; otherwise, it returns False. The unit test `assert text_match_wordz_middle("pythonzabc.")==True` confirms that this function works as expected.