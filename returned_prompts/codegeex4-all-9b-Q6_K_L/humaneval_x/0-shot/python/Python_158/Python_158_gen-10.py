def find_max(words):
    max_len = -1
    max_word = ""
    for word in words:
        if len(set(word)) > max_len:
            max_len = len(set(word))
            max_word = word
        elif len(set(word)) == max_len:
            if word < max_word:
                max_word = word
    return max_word

print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))