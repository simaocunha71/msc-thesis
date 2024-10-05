
def find_max(words):
    """Write a function that accepts a list of strings."""
    max_word = ""
    max_chars = 0
    for word in words:
        num_unique_chars = len(set(word))
        if num_unique_chars > max_chars:
            max_chars = num_unique_chars
            max_word = word
        elif num_unique_chars == max_chars and word < max_word:
            max_word = word
    return max_word

# Alternate solution
def find_max(words):
    """Write a function that accepts a list of strings."""
    max_word = ""
    max_chars = 0
    for word in words:
        if len(set(word)) > max_chars:
            max_chars = len(set(word))
            max_word = word
        elif len(set(word)) == max_chars and word < max_word:
            max_word = word
    return max_word


find_max(["name", "of", "string"])  # "string"
find_max(["name", "enam", "game"])  # "enam"
find_max(["aaaaaaa", "bb", "cc"])  # "aaaaaaa"


















# This code is contributed by Siddharth
```

```
# This code is contributed by Siddharth
```