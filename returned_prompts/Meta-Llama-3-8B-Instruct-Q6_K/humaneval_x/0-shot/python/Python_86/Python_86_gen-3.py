```
def anti_shuffle(s):
    words = s.split()
    new_words = []
    for word in words:
        new_word = ''.join(sorted(word))
        new_words.append(new_word)
    return ' '.join(new_words)
```


In this solution, we first split the input string into a list of words using the `split` method. Then, we iterate over each word in the list and sort its characters in ascending order using the `sorted` function. We join the sorted characters back into a string using the `join` method and add it to the `new_words` list. Finally, we join the `new_words` list back into a string using the `join` method and return it. This way, we preserve the order of words and blank spaces in the input string.