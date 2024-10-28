
def find_max(words):
    unique_chars = set()
    max_unique_chars = 0
    max_word = ""
    for word in words:
        unique_chars = set()
        for char in word:
            if char not in unique_chars:
                unique_chars.add(char)
        if len(unique_chars) > max_unique_chars:
            max_unique_chars = len(unique_chars)
            max_word = word
    return max_word

