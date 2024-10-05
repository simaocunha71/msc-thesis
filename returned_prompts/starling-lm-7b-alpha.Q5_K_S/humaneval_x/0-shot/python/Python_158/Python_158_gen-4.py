
def find_max(words):
    max_words = ""
    max_len = 0
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_len:
            max_len = len(unique_chars)
            max_words = word
        elif len(unique_chars) == max_len:
            if word < max_words:
                max_words = word
    return max_words

# Test Cases
print(find_max(["name", "of", "string"])) # "string"
print(find_max(["name", "enam", "game"])) # "enam"
print(find_max(["aaaaaaa", "bb", "cc"])) # "aaaaaaa"



def find_max(words):
    max_chars = 0
    max_word = ""
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_chars:
            max_chars = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_chars:
            if word < max_word:
                max_word = word
    return max_word
```