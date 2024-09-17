```
def start_withp(words):
    result = []
    for word in words:
        if word.startswith('p'):
            result.append(word.split()[0])
    return tuple(result)
```
This function iterates over the list of words, checks if each word starts with the letter 'p', and if it does, it adds the first word to the result list. Finally, it returns the result as a tuple.

The unit test `assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')` ensures that the function returns the correct words. The words are split into individual words using the `split()` method, and the first word of each word is taken using the `[0]` indexing. The result is then converted to a tuple using the `tuple()` function. 