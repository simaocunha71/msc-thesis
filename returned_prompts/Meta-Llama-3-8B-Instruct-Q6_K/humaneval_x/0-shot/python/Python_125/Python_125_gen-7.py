
The solution is to use the `split()` function to split the string into words. If the string does not contain any spaces, it splits on commas. If it does not contain any commas, it counts the number of lowercase letters with odd order in the alphabet.

Here is the Python code that implements this:

```
def split_words(txt):
    words = txt.split()
    if not words:
        words = txt.replace(',', ' ').split()
    if not words:
        return sum(1 for c in txt.lower() if ord(c) % 2 == 1)
    return words
```

This function first tries to split the string into words using the `split()` function. If the string does not contain any spaces, it splits on commas using the `replace()` function. If the string does not contain any commas, it counts the number of lowercase letters with odd order in the alphabet using a generator expression. Finally, it returns the list of words.