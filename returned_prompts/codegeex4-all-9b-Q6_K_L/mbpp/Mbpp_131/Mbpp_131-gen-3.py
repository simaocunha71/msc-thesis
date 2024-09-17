def reverse_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    vowel_indices = [i for i, char in enumerate(s) if char in vowels]
    vowel_chars = [s[i] for i in vowel_indices]
    vowel_chars.reverse()
    for i, index in enumerate(vowel_indices):
        s = s[:index] + vowel_chars[i] + s[index+1:]
    return s

