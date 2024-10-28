    vowel_replace = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    result = []
    for c in message:
        if c.islower():
            result.append(chr((ord(c) + 1) % 26 + ord('a')) if c not in vowel_replace else vowel_replace[c])
        elif c.isupper():
            result.append(chr((ord(c) + 1) % 26 + ord('A')) if c not in vowel_replace else vowel_replace[c])
        else:
            result.append(c)

    return ''.join(result)


