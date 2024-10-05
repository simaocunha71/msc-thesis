def find_max(words):
    def unique_chars(word):
        return len(set(word))

    max_unique_chars = max(unique_chars(word) for word in words)
    max_words = [word for word in words if unique_chars(word) == max_unique_chars]
    return min(max_words)

print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))