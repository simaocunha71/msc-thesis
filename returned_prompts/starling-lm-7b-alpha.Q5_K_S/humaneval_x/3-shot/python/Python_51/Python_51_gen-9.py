    vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y')
    result = ''
    for char in text:
        if char not in vowels:
            result += char
    return result


