def reverse_vowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].lower() not in vowels:
            i += 1
        elif s[j].lower() not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return ''.join(s)