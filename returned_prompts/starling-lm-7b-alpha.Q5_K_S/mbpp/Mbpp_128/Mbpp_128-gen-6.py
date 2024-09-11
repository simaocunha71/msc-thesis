```python
def long_words(n, string):
    list = string.split()
    result = []
    for i in list:
        if len(i) > n:
            result.append(i)
    return result
```

Explanation:
This function takes in two parameters: n, the length of the words you want to find, and string, the list of words. It splits the string into a list of words using the split() method. Then, it iterates over the list and checks the length of each word. If the length is greater than n, it adds the word to the result list. Finally, it returns the result list.

The assert statement checks if the function works correctly by passing in a sample string and comparing the output with the expected result.

In this case, the function is called with the arguments 3 and "python is a programming language". The string is split into the list ["python", "is", "a", "programming", "language"]. The function then adds the words "python", "programming", and "language" to the result list, as their lengths are greater than 3. The function returns the result list, which is ['python', 'programming', 'language']. The assert statement checks if this is the correct output and passes if it is.

Overall, the function correctly finds and returns all the words in the given string that are longer than the specified length.

```python
def long_words(n, string):
    list = string.split()
    result = []
    for i in list:
        if len(i) > n:
            result.append(i)
    return result
```

This code defines a function called `long_words` that takes in two parameters: `n` and `string`. The function first splits the `string` into a list of words using the `split()` method. It then initializes an empty list called `result` to store the words that are longer than `n` characters. 

The function then iterates over each word in the `list` using a for loop. For each word, it checks if the length of the word (`len(i)`) is greater than `n`. If it is, the word is added to the `result` list using the `append()` method