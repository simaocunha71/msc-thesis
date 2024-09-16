```
def capital_words_spaces(string):
    words = string.split()
    for i in range(len(words)):
        words[i] = ' '+words[i]
    return ''.join(words)
```
