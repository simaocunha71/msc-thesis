```
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonants = 0
        for char in word:
            if char.isalpha() and char.lower() not in 'aeiou':
                consonants += 1
        if consonants == n:
            result.append(word)
    return result
```


Explanation:
The function `select_words` takes a string `s` and an integer `n` as inputs. It first splits the string into words using the `split` method. Then, it initializes an empty list `result` to store the words that contain exactly `n` consonants.

The function then iterates over each word in the list of words. For each word, it counts the number of consonants by iterating over each character in the word and checking if the character is a letter (using the `isalpha` method) and not a vowel (using the `lower` method to convert the character to lowercase and checking if it is not in the string 'aeiou'). If the number of consonants is equal to `n`, the word is added to the `result` list.

Finally, the function returns the `result` list.

The function handles the edge case where the input string is empty by returning an empty list. It also handles the case where the input string contains only spaces by returning an empty list. The function is case-insensitive, so it treats uppercase and lowercase letters as the same. It also ignores punctuation and special characters. The function returns the words in the order they appear in the input string.