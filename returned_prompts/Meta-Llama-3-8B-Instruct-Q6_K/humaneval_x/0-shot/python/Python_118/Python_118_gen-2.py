def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    for i in range(len(word) - 1, -1, -1):
        if word[i] in vowels:
            if word[i-1] not in vowels and word[i+1] not in vowels:
                return word[i]
    return ""
# Test cases
print(get_closest_vowel("yogurt")) # "u"
print(get_closest_vowel("FULL")) # "U"
print(get_closest_vowel("quick")) # ""
print(get_closest_vowel("ab")) # ""
print(get_closest_vowel("hello")) # "o" 
print(get_closest_vowel("bcdfgh")) # ""
print(get_closest_vowel("a")) # ""
print(get_closest_vowel("z")) # "" 
print(get_closest_vowel("aeiou")) # "" 
print(get_closest_vowel("bc")) # ""
print(get_closest_vowel("xyz")) # ""
print(get_closest_vowel("AEIOU")) # ""
print(get_closest_vowel("BCDFGH")) # ""
print(get_closest_vowel("AEIOUbcdfgh")) # ""
print(get_closest_vowel("AEIOUbcd")) # "A"
print(get_closest_vowel("aeiouBCDFGH")) # ""
print(get_closest_vowel("a")) # ""
print(get_closest_vowel("AEIOU")) # ""
print(get_closest_vowel("bcdfgh")) # ""
print(get_closest_vowel("a")) # ""
print(get_closest_vowel("AEIOU")) # ""
print(get_closest_vowel("bcdfgh")) # ""
print(get_closest_vowel("aeiou")) # ""
print(get_closest_vowel("bcdfgh")) # ""
print(get_closest_vowel("AEIOU")) # ""
print(get_closest_vowel("bcdfgh")) # ""
print(get_closest_vowel("a")) # ""
print(get_closest_vowel("AEIOU")) # ""
print(get_closest_vowel("bcdfgh")) # ""
print(get_closest_vowel("aeiou")) # ""
print(get_closest_vowel("bcdfgh")) # ""
print(get_closest_vowel("AEIOU")) # ""
print(get_closest_vowel("bcdfgh")) # ""
print(get_closest_vowel("a")) # ""
print(get_closest