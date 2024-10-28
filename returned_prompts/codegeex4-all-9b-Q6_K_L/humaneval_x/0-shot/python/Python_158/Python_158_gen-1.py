def find_max(words):
    def count_unique_chars(word):
        return len(set(word))

    max_unique_chars = max(count_unique_chars(word) for word in words)
    return min((word for word in words if count_unique_chars(word) == max_unique_chars), key=lambda x: x.lower())

print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))