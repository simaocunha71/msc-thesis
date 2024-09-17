```
def remove_length(s, k):
    words = s.split()
    result = ''
    for word in words:
        if len(word) != k:
            result += word + ' '
    return result.strip()
```


This function splits the given string into words, then iterates over each word. If the length of the word is not equal to k, it adds the word to the result string. Finally, it returns the result string with leading and trailing spaces removed. The unit test `assert remove_length('The person is most value tet', 3) == 'person is most value'` helps to clarify the expected behavior of the function. For example, it shows that the function should return the string 'person is most value' when given the string 'The person is most value tet' and k = 3. This is because 'The' and 'tet' are the words of length 3 in the string, and they should be removed.