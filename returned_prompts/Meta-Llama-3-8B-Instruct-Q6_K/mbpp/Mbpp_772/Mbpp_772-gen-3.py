```
def remove_length(s, k):
    words = s.split()
    result = []
    for word in words:
        if len(word) != k:
            result.append(word)
    return ' '.join(result)
```



The given problem is to create a function that removes all the words with a specific length (k) from a given string. 

The function `remove_length` takes two parameters: `s` which is the input string and `k` which is the length of the words to be removed. The function splits the input string into words, then iterates over each word. If the length of the word is not equal to `k`, the word is added to the result list. Finally, the function joins the result list with spaces to form the output string.

The unit test `assert remove_length('The person is most value tet', 3) == 'person is most value'` helps to understand the problem better. It shows that the function should remove all words with length 3 from the input string and return the resulting string. 

Here is the Python code for the solution:

```
def remove_length(s, k):
    words = s.split()
    result = []
    for word in words:
        if len(word) != k:
            result.append(word)
    return ' '.join(result)
```



This function will return the string with all words of length `k` removed. For example, if you call `remove_length('The person is most value tet', 3)`, it will return `'person is most value'`. This is because 'The' and 'tet' are the only words of length 3 in the input string, and they are removed from the output. 