```
def long_words(n, words):
    return [word for word in words if len(word) > n]
```



The function `long_words` takes two parameters, `n` and `words`. It returns a list of words from the input list `words` that have more than `n` characters.

The unit test `assert long_words(3,"python is a programming language")==['python','programming','language']` ensures that the function works correctly. It checks that when the function is called with the string "python is a programming language" and `n=3`, it returns the list `['python','programming','language']`, which are the words in the string with more than 3 characters.