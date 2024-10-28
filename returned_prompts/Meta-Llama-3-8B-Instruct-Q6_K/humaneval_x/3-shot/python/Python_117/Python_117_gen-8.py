    vowels = 'aeiouAEIOU'
    result = []
    word = ''
    for char in s.split():
        for c in char:
            if c not in vowels:
                word += c
            else:
                if len(word) == n:
                    result.append(char)
                word = ''
    if len(word) == n:
        result.append(char)
    return result


