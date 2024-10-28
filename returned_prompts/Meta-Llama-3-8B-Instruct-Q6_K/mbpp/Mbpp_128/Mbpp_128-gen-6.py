```
def long_words(n, sentence):
    words = sentence.split()
    result = [word for word in words if len(word) > n]
    return result
```
The function `long_words` takes two parameters: `n` which is the maximum length of words, and `sentence` which is the input sentence. It first splits the sentence into a list of words. Then, it uses a list comprehension to create a new list that includes only the words with length greater than `n`. The function returns this new list. The unit test `assert long_words(3,"python is a programming language")==['python','programming','language']` ensures that the function works correctly.  It checks if the words in the input sentence that have length greater than 3 are correctly returned.  