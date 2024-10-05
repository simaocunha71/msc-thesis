def get_closest_vowel(word):
    vowels = "AEIOUaeiou"
    for i in range(len(word) - 2, 0, -1):  # Start from the second last character
        if word[i] in vowels:
            if word[i-1] not in vowels and word[i+1] not in vowels:
                return word[i]
    return ""

# Test cases
print(get_closest_vowel("yogurt"))  # "u"
print(get_closest_vowel("FULL"))  # "U"
print(get_closest_vowel("quick"))  # ""
print(get_closest_vowel("ab"))  # ""