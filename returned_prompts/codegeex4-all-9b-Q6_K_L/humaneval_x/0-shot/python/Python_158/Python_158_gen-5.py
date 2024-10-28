def find_max(words):
    max_len = -1
    max_word = ""
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_len or (len(unique_chars) == max_len and word < max_word):
            max_len = len(unique_chars)
            max_word = word
    return max_word

print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))