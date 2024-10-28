```
def find_max(words):
    max_len = 0
    max_word = ''
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_len:
            max_len = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_len:
            max_word = min(max_word, word)
    return max_word
```


This function iterates over the list of words. For each word, it calculates the number of unique characters using the set function. If the number of unique characters is greater than the current maximum, it updates the maximum and the corresponding word. If the number of unique characters is equal to the current maximum, it updates the maximum word to be the lexicographically smaller one. Finally, it returns the word with the maximum number of unique characters. If there are multiple words with the maximum number of unique characters, it returns the lexicographically smaller one. 

The function handles the edge case where the input list is empty by not returning anything in that case. It also handles the edge case where all words have the same number of unique characters by returning the lexicographically smaller one. 

The time complexity of this function is O(n*m), where n is the number of words and m is the maximum length of a word. This is because for each word, it calculates the number of unique characters, which takes O(m) time. The space complexity is O(m), where m is the maximum length of a word. This is because it uses a set to store the unique characters in a word. 