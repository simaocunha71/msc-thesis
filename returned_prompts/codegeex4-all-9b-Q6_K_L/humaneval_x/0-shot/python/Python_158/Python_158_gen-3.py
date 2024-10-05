def find_max(words):
    def unique_chars(word):
        return len(set(word))

    return min(words, key=unique_chars)

print(find_max(["name", "of", "string"]))  # "string"
print(find_max(["name", "enam", "game"]))  # "enam"
print(find_max(["aaaaaaa", "bb" ,"cc"]))  # "aaaaaaa"