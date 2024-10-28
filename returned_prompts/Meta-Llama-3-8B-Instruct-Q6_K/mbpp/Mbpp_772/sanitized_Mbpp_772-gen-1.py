def remove_length(s, k):
    words = s.split()
    result = ' '.join([word for word in words if len(word) != k])
    return result