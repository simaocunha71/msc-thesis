```
def find_max(words):
    max_word = ""
    max_unique_chars = 0
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_unique_chars:
            max_unique_chars = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_unique_chars:
            if word < max_word:
                max_word = word
    return max_word
```
The function `find_max` iterates over each word in the input list. For each word, it calculates the number of unique characters using a set. If the number of unique characters is greater than the current maximum, it updates the maximum word and the maximum number of unique characters. If the number of unique characters is equal to the current maximum, it checks if the word comes before the current maximum word in lexicographical order. If it does, it updates the maximum word. Finally, it returns the maximum word. If no words have unique characters (i.e., the list only contains repeated characters), the function returns an empty string. 