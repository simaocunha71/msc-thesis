```
def remove_length(s, k):
    words = s.split()
    result = []
    for word in words:
        if len(word) != k:
            result.append(word)
    return ' '.join(result)
```
The function `remove_length` takes a string `s` and an integer `k` as arguments. It splits the string into words and then iterates over each word. If the length of the word is not equal to `k`, it adds the word to the result list. Finally, it joins the words in the result list with a space and returns the resulting string. The unit test `assert remove_length('The person is most value tet', 3) == 'person is most value'` ensures that the function works correctly.  For example, if `s='The person is most value tet'` and `k=3`, the function should return `'person is most value'`.  



