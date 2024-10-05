```
def find_max(words):
    max_length = 0
    max_word = None
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_length:
            max_length = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_length:
            if word < max_word:
                max_word = word
    return max_word
```


The provided solution defines a function `find_max` that accepts a list of strings. It iterates over the list, and for each word, it calculates the number of unique characters using the `set` data structure. If the number of unique characters is greater than the current maximum, it updates the maximum length and the maximum word. If the number of unique characters is equal to the current maximum, it checks if the current word is lexicographically smaller than the maximum word and updates the maximum word if necessary. Finally, it returns the maximum word. If all words have the same number of unique characters, the function returns the first word in lexicographical order.