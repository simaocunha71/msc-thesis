```
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonants = 0
        for char in word:
            if char.lower() not in 'aeiou':
                consonants += 1
        if consonants == n:
            result.append(word)
    return result
```





This function first splits the input string into a list of words. Then, for each word, it counts the number of consonants. If the number of consonants is equal to the given number n, the word is added to the result list. Finally, the function returns the list of words that contain exactly n consonants. If the input string is empty, the function returns an empty list.