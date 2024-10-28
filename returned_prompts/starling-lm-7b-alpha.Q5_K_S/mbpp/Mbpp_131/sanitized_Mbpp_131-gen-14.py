def reverse_vowels(s: str) -> str:
    vowels = "aeiou"
    rev_vowels = s[::-1]
    return "".join(i if i in vowels else rev_vowels[vowels.find(i)] for i in s)