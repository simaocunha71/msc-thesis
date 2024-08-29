def remove_length(string, k):
    return " ".join([word for word in string.split() if len(word) != k])