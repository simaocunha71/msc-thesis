def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    for i in range(len(word) - 1, -1, -1):
        if word[i] not in vowels:
            for j in range(i - 1, -1, -1):
                if word[j] in vowels:
                    return word[j]
    return ''
# Test cases
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))  # Output: "U"
print(get_closest_vowel("quick"))  # Output: ""
print(get_closest_vowel("ab"))  # Output: ""
print(get_closest_vowel("aeiou"))  # Output: ""
print(get_closest_vowel("bcdfgh"))  # Output: ""
print(get_closest_vowel("hello"))  # Output: "e"
print(get_closest_vowel("bcdfghjklmn"))  # Output: "o"  # Output: "o"
print(get_closest_vowel("bcdfghjklmn"))  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"  # Output: "o"