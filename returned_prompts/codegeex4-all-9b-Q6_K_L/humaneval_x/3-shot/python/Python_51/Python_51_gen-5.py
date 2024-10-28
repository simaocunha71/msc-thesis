    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    result = ''
    for c in text:
        if c.lower() not in vowels:
            result += c
    return result

