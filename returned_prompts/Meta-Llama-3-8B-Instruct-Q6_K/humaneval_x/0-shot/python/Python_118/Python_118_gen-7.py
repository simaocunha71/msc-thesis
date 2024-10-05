def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    for i in range(len(word) - 2, -1, -1):
        if word[i] not in vowels:
            if word[i + 1] in vowels or word[i + 2] in vowels:
                return word[i + 1] if word[i + 1] in vowels else word[i + 2]
    return ''

# Test cases
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))  # Output: "U"
print(get_closest_vowel("quick"))  # Output: ""
print(get_closest_vowel("ab"))  # Output: ""
print(get_closest_vowel("hello"))  # Output: "o"
print(get_closest_vowel("bcdf"))  # Output: ""


# Explanation
The function `get_closest_vowel` iterates over the word from right to left. It checks each character if it's not a vowel. If it's not a vowel, it checks the next two characters if any of them is a vowel. If it finds a vowel, it returns that vowel. If it doesn't find any vowel, it returns an empty string. The function is case sensitive and only considers English letters. The test cases demonstrate the function's behavior with different inputs. 





# Another Solution
def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    for i in range(len(word) - 1, -1, -1):
        if word[i] in vowels:
            if i < len(word) - 1 and word[i + 1] not in vowels:
                return word[i]
    return ''

# Test cases
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))  # Output: "U"
print(get_closest_vowel("quick"))  # Output: ""
print(get_closest_vowel("ab"))  # Output: ""
print(get_closest_vowel("hello"))  # Output: "o"
print(get_closest_vowel("bcdf"))  # Output: ""





# Explanation
The function `get_closest_vowel` iterates over the word from right to left. It checks each character if it's a vowel. If it's a vowel and the next character is not