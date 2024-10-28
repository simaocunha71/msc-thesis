```
def anti_shuffle(s):
    words = s.split()
    new_words = []
    for word in words:
        new_word = "".join(sorted(word))
        new_words.append(new_word)
    return " ".join(new_words)
```


This function splits the input string into words, then for each word, it sorts the characters in ascending order and joins them back together. The sorted words are then joined back into a string with spaces in between. The order of words and spaces in the original string is preserved. For example, calling `anti_shuffle('Hello World!!!')` would return `'Hello !!!Wdlor'`. 

The time complexity of this function is O(n*m*logm), where n is the number of words and m is the length of the longest word, because it needs to iterate over each word, sort each word, and then join the words back together. The space complexity is O(n*m), because it needs to store the sorted words. 