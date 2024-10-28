def remove_length(string, k):
    words = string.split()
    words = [word for word in words if len(word) != k]
    return ' '.join(words)