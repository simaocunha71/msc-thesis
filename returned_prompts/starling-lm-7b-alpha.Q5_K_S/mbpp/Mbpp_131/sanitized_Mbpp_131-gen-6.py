def reverse_vowels(s):
    """
    Reverse only the vowels in a given string.
    """
    vowels = "aeiouAEIOU"
    i, j = 0, len(s) - 1
    s = list(s)
    while i < j:
        if s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return "".join(s)