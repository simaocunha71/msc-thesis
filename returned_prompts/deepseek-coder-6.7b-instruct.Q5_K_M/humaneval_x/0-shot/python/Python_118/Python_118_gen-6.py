
    def get_closest_vowel(word):
        vowels = 'aeiouAEIOU'
        word = word[::-1]
        for i in range(1, len(word) - 1):
            if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
                return word[i]
        return ""

    print(get_closest_vowel("yogurt"))  # ==> "u"
    print(get_closest_vowel("FULL"))  # ==> "U"
    print(get_closest_vowel("quick"))  # ==> ""
    print(get_closest_vowel("ab"))  # ==> ""

The function get_closest_vowel first reverses the word so that it starts from the right side and traverses from right to left. Then it iterates through the word from the second character to the second last character. If the current character (word[i]) is a vowel and the character before it (word[i - 1]) and the character after it (word[i + 1]) are not vowels, it returns the character. If no such character is found, it returns an empty string.

This is a simple solution and should work for all the given examples.
"""

# ---------------------
# Code to reverse a word
# ---------------------


def reverse_word(word):
    return word[::-1]


print(reverse_word("hello"))
print(reverse_word("python"))
print(reverse_word("world"))

# ---------------------
# Code to find the vowels in a word
# ---------------------


def find_vowels(word):
    vowels = "aeiou"
    return [letter for letter in word if letter.lower() in vowels]


print(find_vowels("hello"))
print(find_vowels("python"))
print(find_vowels("world"))

# ---------------------
# Code to find the consonants in a word
# ---------------------


def find_