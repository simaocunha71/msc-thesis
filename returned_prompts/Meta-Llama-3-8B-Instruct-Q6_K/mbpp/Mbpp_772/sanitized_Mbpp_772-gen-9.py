def remove_length(s, k):
    words = s.split()
    result = []
    for word in words:
        if len(word) != k:
            result.append(word)
    return ' '.join(result)  # or return result if you want a list of words