
```
def get_closest_vowel(word):
    word = word.lower()
    vowels = "aeiou"
    for i in range(len(word) - 1, -1, -1):
        if word[i] in vowels:
            if i > 0 and word[i - 1] not in vowels and word