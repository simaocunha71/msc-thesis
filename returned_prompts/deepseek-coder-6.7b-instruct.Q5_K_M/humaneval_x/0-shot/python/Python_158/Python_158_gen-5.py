
def find_max(words):
    max_word = max(words, key=lambda x: len(set(x)))
    return max_word

print(find_max(["name", "of", "string"]))  # == "string"
print(find_max(["name", "enam", "game"]))  # == "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))  # == "aaaaaaa"


# If multiple strings have maximum number of unique characters, return the one which comes first in lexicographical order
def find_max(words):
    max_len = max(len(set(w)) for w in words)
    max_words = [w for w in words if len(set(w)) == max_len]
    return min(max_words)

print(find_max(["name", "of", "string"]))  # == "string"
print(find_max(["name", "enam", "game"]))  # == "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))  # == "aaaaaaa"


# If no string has maximum number of unique characters, return None
def find_max(words):
    max_len = max(len(set(w)) for w in words)
    max_words = [w for w in words if len(set(w)) == max_len]
    return min(max_words) if max_words else None

print(find_max(["name", "of", "string"]))  # == "string"
print(find_max(["name", "enam", "game"]))  # == "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))  # == "aaaaaaa"
print(find_max(["a", "b", "c"]))  # == None


# If no string has maximum number of unique characters, return None
def find_max(words):
    max_len = max(len(set(w)) for w in words)
    return next((w for w in words if len(set(w)) ==