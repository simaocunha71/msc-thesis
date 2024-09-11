def remove_length(s, k):
    return ' '.join([word for word in s.split() if len(word) != k])  # filter words with length k and join the remaining words with spaces