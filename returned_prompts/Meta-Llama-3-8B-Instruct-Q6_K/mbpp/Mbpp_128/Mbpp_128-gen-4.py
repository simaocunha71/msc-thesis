```
def long_words(n, words):
    return [word for word in words.split() if len(word) > n]
```


The function `long_words` takes two parameters: `n`, which is the length threshold, and `words`, which is a string of words separated by spaces. It returns a list of words that are longer than `n` characters. The function uses list comprehension to iterate over the words, split the string into words, and filter out the words that are shorter than or equal to `n` characters.

For example, if you call `long_words(3, "python is a programming language")`, it will return `['python', 'programming', 'language']`, which are the words that are longer than 3 characters. The unit test `assert long_words(3,"python is a programming language")==['python','programming','language']` ensures that the function works correctly.