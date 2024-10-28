
def get_closest_vowel(word):
    vowels = "AEIOUaeiou"
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels:
            return word[i]
    return ""

# Test cases
print(get_closest_vowel("yogurt"))  # "u"
print(get_closest_vowel("FULL"))   # "U"
print(get_closest_vowel("quick"))  # ""
print(get_closest_vowel("ab"))     # ""



















```  
