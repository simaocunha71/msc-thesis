def remove_length(s, k):
    words = s.split()
    result = ''
    for word in words:
        if len(word) != k:
            result += word + ' '
    return result.strip()