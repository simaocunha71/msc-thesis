
def reverse_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    s = list(s)
    for i in range(len(s)):
        if s[i] in vowels:
            j = len(s) - 1 - i
            while s[j] not in vowels:
                j -= 1
            s[i], s[j] = s[j], s[i]
    return ''.join(s)


