```
def find_max(words):
    max_word = ""
    max_chars = 0
    for word in words:
        chars = set(word)
        if len(chars) > max_chars:
            max_chars = len(chars)
            max_word = word
        elif len(chars) == max_chars:
            max_word = min(max_word, word)
    return max_word
```


This function iterates over each word in the input list. For each word, it calculates the number of unique characters (using the `set` function) and checks if it's greater than the current maximum. If it is, it updates the maximum word. If the number of unique characters is equal to the current maximum, it checks if the word is lexicographically smaller than the current maximum word and updates the maximum word if it is. Finally, it returns the maximum word. If no words have unique characters, it returns an empty string.