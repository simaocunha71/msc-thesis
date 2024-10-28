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
            if word < max_word:
                max_word = word
    return max_word
```





Explanation:

1. Initialize an empty string `max_word` to store the word with the maximum number of unique characters.
2. Initialize an integer `max_unique_chars` to store the maximum number of unique characters found so far.
3. Iterate through each word in the input list `words`.
4. For each word, calculate the set of unique characters using the `set` function.
5. If the length of the set of unique characters is greater than `max_unique_chars`, update `max_word` and `max_unique_chars` with the current word and its unique character count.
6. If the length of the set of unique characters is equal to `max_unique_chars`, compare the current word with `max_word` lexicographically. If the current word is smaller, update `max_word`.
7. Return `max_word` as the result.

The time complexity of this function is O(n), where n is the length of the input list, because we are iterating through each word once. The space complexity is O(m), where m is the maximum length of a word, because we are storing the set of unique characters for each word.