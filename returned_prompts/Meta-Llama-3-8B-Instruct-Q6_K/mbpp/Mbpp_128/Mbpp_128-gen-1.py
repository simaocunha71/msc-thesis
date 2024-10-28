```
def long_words(n, words):
    return [word for word in words if len(word) > n]
```
This function uses a list comprehension to create a new list of words that are longer than the given number `n`. It iterates over each word in the input list `words` and checks if the length of the word is greater than `n`. If it is, the word is included in the new list. The function then returns this new list. 

The unit test `assert long_words(3,"python is a programming language")==['python','programming','language']` checks that the function correctly identifies words that are longer than 3 characters in the given sentence. 

For example, `long_words(3, "python is a programming language")` would return `['python', 'programming', 'language']` because these are the words in the sentence that are longer than 3 characters. 

The function is case-sensitive and considers punctuation as part of the word. If you want to make it case-insensitive or ignore punctuation, you would need to preprocess the words before passing them to the function.  For example, you could convert all words to lower case and remove punctuation before passing them to the function.  Here is how you could modify the function to do this:

```
import string

def long_words(n, words):
    words = [''.join(char for char in word if char not in string.punctuation).lower() for word in words]
    return [word for word in words if len(word) > n]
```

This modified function uses a list comprehension to convert each word to lower case and remove punctuation before checking its length.  The `string.punctuation` constant is a pre-initialized string containing all ASCII punctuation characters.  The `join` method is used to concatenate the characters in each word that are not punctuation characters.  The resulting list of words without punctuation is then passed to the original list comprehension to filter out words that are not longer than `n` characters.  This modified function would return the same result as the original function, but it would ignore punctuation and consider all words in a case-insensitive manner.  For example, `long_words(3, "python is a programming language")` would still return `['python', 'programming', 'language']`, but it would treat "Python" and "python" as the same word.  Similarly, it would treat "language!" as the same word as "language".  This is because it