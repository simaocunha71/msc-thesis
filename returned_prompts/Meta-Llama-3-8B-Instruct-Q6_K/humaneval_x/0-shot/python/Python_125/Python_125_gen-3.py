
The problem is asking to split a string of words into a list of words. If there are no whitespaces in the string, it should split on commas. If there are no commas, it should return the number of lowercase letters with odd order in the alphabet.

Here is a Python solution for the problem:

```
def split_words(txt):
    words = txt.split()
    if not words and ',' in txt:
        words = txt.split(',')
        if len(words) > 1:
            words = [word.strip() for word in words]
    if not words:
        return sum(1 for i in range(ord('a'), ord('z')+1) if txt.count(chr(i)) % 2 != 0)
    return words
```

This function first tries to split the string on whitespaces using the `split()` method. If the resulting list is empty and the string contains commas, it tries to split the string on commas. If the resulting list is still empty, it counts the number of lowercase letters with odd order in the alphabet using a generator expression. If the list is not empty, it returns the list of words.