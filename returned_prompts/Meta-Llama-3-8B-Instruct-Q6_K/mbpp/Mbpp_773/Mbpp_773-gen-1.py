```
def occurance_substring(text, substring):
    if substring in text:
        return substring, text.index(substring), text.index(substring) + len(substring)
    else:
        return None
```

This function checks if the substring is present in the text. If it is, it returns a tuple containing the substring, its starting position, and its ending position. If not, it returns None. The unit test `assert occurance_substring('python programming, python language','python')==('python', 0, 6)` ensures the function works correctly. 

The `index` method of a string returns the index of the first occurrence of the substring. We use this method to get the starting position of the substring. To get the ending position, we add the length of the substring to the starting position. If the substring is not found, the `in` operator returns False and the function returns None. 

This function is case-sensitive and does not handle overlapping occurrences. For example, if the substring is 'py' and the text is 'python', the function will return the first 'py' but not the second one. If you want to handle overlapping occurrences or make the function case-insensitive, you would need to modify it accordingly. 