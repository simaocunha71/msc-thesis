def remove_length(string, k):
    """
    Remove all the words with k length in the given string
    """
    words = string.split()
    new_words = []
    for word in words:
        if len(word) != k:
            new_words.append(word)
    return " ".join(new_words)