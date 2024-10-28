```
def anti_shuffle(s):
    words = s.split()
    new_words = []
    for word in words:
        new_word = ''.join(sorted(word))
        new_words.append(new_word)
    return ' '.join(new_words)
```


The function works as follows:
1. It splits the input string into a list of words using the `split()` method.
2. It iterates over each word in the list and sorts the characters in the word using the `sorted()` function.
3. It joins the sorted characters back into a string using the `join()` method.
4. It appends the new word to a list of new words.
5. It joins the list of new words back into a string using the `join()` method, with spaces in between each word.
6. It returns the resulting string.