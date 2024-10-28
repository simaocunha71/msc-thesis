```
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonants = sum(1 for char in word if char.lower() not in 'aeiou ')
        if consonants == n:
            result.append(word)
    return result
```



The function `select_words` takes two parameters: a string `s` and an integer `n`. It first splits the string `s` into a list of words using the `split` method. Then, for each word in the list, it counts the number of consonants using a generator expression. If the number of consonants matches the given integer `n`, the word is added to the result list. Finally, the function returns the list of words that contain exactly `n` consonants.

The `sum` function is used to count the number of consonants in each word. The generator expression inside the `sum` function iterates over each character in the word and checks if the character is not in the string 'aeiou ' (i.e., it is a consonant). The `lower` method is used to make the check case-insensitive.

The function returns an empty list if the input string is empty, as required. The examples provided in the problem statement are also handled correctly by the function. For example, `select_words("Mary had a little lamb", 4)` returns `["little"]`, `select_words("Mary had a little lamb", 3)` returns `["Mary", "lamb"]`, and so on.