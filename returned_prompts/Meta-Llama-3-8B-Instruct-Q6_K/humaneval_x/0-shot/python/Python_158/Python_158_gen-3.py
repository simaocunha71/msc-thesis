```
def find_max(words):
    max_word = ""
    max_unique_chars = 0
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_unique_chars:
            max_word = word
            max_unique_chars = len(unique_chars)
        elif len(unique_chars) == max_unique_chars:
            max_word = min(max_word, word)
    return max_word
```


The function `find_max` iterates over the list of words. For each word, it calculates the number of unique characters using a set. If the number of unique characters in the current word is greater than the maximum number of unique characters found so far, it updates the maximum word and the maximum number of unique characters. If the number of unique characters is equal to the maximum number of unique characters found so far, it updates the maximum word to be the lexicographically smaller one. Finally, it returns the maximum word. If the list is empty, it returns an empty string.

The function is tested with the provided test cases:
```
print(find_max(["name", "of", "string"])) # "string"
print(find_max(["name", "enam", "game"])) # "enam"
print(find_max(["aaaaaaa", "bb", "cc"])) # "aaaaaaa"
print(find_max([])) # ""
```


The function passes all the test cases. It correctly identifies the word with the maximum number of unique characters and returns the lexicographically smallest one if there are multiple words with the maximum number of unique characters. If the list is empty, it returns an empty string. 