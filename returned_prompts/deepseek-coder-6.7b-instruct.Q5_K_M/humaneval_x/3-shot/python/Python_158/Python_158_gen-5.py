    max_len = max([len(set(word)) for word in words])
    max_words = [word for word in words if len(set(word)) == max_len]
    return min(max_words)


