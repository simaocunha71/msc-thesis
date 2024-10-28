def reverse_vowels(s):
    vowels = "aeiou"
    result = ""
    for c in s:
        if c in vowels:
            result = c + result
        else:
            result += c
    return result