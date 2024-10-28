def reverse_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    rev_vowels = vowels[::-1]
    for i in range(len(s)):
        if s[i] in vowels:
            s[i] = rev_vowels[vowels.index(s[i])]
    return "".join(s)