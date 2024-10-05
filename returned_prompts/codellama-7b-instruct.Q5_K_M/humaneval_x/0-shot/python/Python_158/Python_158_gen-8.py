
def find_max(words):
    max_unique = 0
    max_unique_word = ""
    for word in words:
        if len(set(word)) > max_unique:
            max_unique = len(set(word))
            max_unique_word = word
    return max_unique_word
