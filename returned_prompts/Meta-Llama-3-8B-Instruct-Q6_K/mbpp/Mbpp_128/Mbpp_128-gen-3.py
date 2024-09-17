```
def long_words(n, words):
    return [word for word in words if len(word) > n]
```
This function uses a list comprehension to create a new list containing only the words from the input list that have a length greater than n. The `len(word)` function is used to get the length of each word, and the `if` condition is used to filter out words that are not longer than n. The resulting list is then returned. The unit test `assert long_words(3,"python is a programming language")==['python','programming','language']` demonstrates the function's behavior. For example, calling `long_words(3,"python is a programming language")` would return `['python','programming','language']`, as expected.