
def find_max(words):
    max_length = 0
    result = ""
    for word in words:
        if len(set(word)) > max_length:
            max_length = len(set(word))
            result = word
    return result
