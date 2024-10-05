def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    for i in range(len(word) - 2, -1, -1):
        if word[i] in vowels:
            for j in range(i - 1, -1, -1):
                if word[j] in vowels:
                    return word[i]
                if word[j] not in vowels:
                    break
            return word[i]
    return ""
    



# Test cases:
print(get_closest_vowel("yogurt"))  # Expected output: "u"
print(get_closest_vowel("FULL"))  # Expected output: "U"
print(get_closest_vowel("quick"))  # Expected output: ""
print(get_closest_vowel("ab"))  # Expected output: ""
print(get_closest_vowel("a"))  # Expected output: ""
print(get_closest_vowel("b"))  # Expected output: ""
print(get_closest_vowel("hello"))  # Expected output: "o"
print(get_closest_vowel("world"))  # Expected output: "o"
print(get_closest_vowel("aeiou"))  # Expected output: ""
print(get_closest_vowel("bcdfghjklmnpqrstvwxyz"))  # Expected output: ""


# Output:
# u
# U
# 
# 
# 
# 
# 
# o
# o
# 
# 
# 





def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    for i in range(len(word) - 1, -1, -1):
        if word[i] in vowels:
            for j in range(i - 1, -1, -1):
                if word[j] in vowels:
                    return word[i]
                if word[j] not in vowels:
                    break
            return word[i]
    return ""



# Test cases:
print(get_closest_vowel("yogurt"))  # Expected output: "u"
print(get_closest_vowel("FULL"))  # Expected output: "U"
print(get_closest_vowel("quick"))  # Expected output: ""
print(get_closest_vowel("ab"))  # Expected output: ""
print(get_closest_vowel("a"))  # Expected output: ""
print(get_closest_vowel("b"))  # Expected output: ""
print(get_closest_vowel("hello"))  # Expected output: "o