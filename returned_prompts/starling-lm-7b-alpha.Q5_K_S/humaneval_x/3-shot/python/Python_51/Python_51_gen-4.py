    vowels = ('a', 'e', 'i', 'o', 'u')
    result = ''
    for char in text:
        if char not in vowels:
            result += char
    return result


