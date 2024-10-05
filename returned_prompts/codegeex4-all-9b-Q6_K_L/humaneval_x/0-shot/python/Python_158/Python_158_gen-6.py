def find_max(words):
    unique_chars = [(set(word), word) for word in words]
    unique_chars.sort(key=lambda x: (-len(x[0]), x[1]))
    return unique_chars[0][1]

print(find_max(["name", "of", "string"]))  # "string"
print(find_max(["name", "enam", "game"]))  # "enam"
print(find_max(["aaaaaaa", "bb" ,"cc"]))  # "aaaaaaa"