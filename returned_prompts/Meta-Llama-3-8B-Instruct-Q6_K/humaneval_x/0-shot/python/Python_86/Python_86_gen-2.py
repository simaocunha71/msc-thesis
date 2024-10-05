```
def anti_shuffle(s):
    words = s.split()
    result = []
    for word in words:
        result.append(''.join(sorted(word)))
    return ' '.join(result)
```


This function works by first splitting the input string into a list of words using the `split` method. Then, for each word in the list, it sorts the characters in the word using the `sorted` function and joins them back together into a string using the `join` method. The resulting list of strings is then joined back together with spaces in between using the `join` method to form the final output string.