def remove_length(s, k):
    words = s.split()
    result = [word for word in words if len(word) != k]
    return ' '.join(result)