    words = s.split()
    result = []
    for word in words:
        char_list = sorted(word)
        result.append(''.join(char_list))
    return ' '.join(result)


