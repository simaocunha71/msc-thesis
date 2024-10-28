def reverse_vowels(s):
    vowels = "aeiou"
    i, j = 0, len(s)-1
    s = list(s)
    while i < j:
        while s[i] not in vowels:
            i += 1
        while s[j] not in vowels:
            j -= 1
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return "".join(s)