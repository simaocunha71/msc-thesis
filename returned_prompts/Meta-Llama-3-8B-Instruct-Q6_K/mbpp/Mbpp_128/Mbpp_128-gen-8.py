```
def long_words(n, words):
    return [word for word in words if len(word) > n]
```
This function takes two parameters: `n` (the length threshold) and `words` (a list of words). It uses a list comprehension to create a new list containing only the words that are longer than `n` characters. The `len(word) > n` condition checks if the length of each word is greater than `n`. If it is, the word is included in the new list.

For example, if you call `long_words(3, ["python", "is", "a", "programming", "language"])`, the function will return `["python", "programming", "language"]`, because these are the words that are longer than 3 characters. The other words in the list are shorter than 3 characters and are not included in the result.