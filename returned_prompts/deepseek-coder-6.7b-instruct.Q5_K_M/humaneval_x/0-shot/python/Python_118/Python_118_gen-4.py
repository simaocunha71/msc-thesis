
def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    word = word[::-1]
    for i in range(1, len(word) - 1):
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            return word[i]
    return ''

# Test cases
print(get_closest_vowel("yogurt"))  # ==> "u"
print(get_closest_vowel("FULL"))  # ==> "U"
print(get_closest_vowel("quick"))  # ==> ""
print(get_closest_vowel("ab"))  # ==> ""

In this solution, we first reverse the input word. Then we iterate from the second character to the second-last character of the reversed word. For each character, we check if it is a vowel and both the previous and next characters are not vowels (i.e., it is a consonant surrounded by vowels from the right side). If we find such a character, we return it. If we do not find any such character, we return an empty string.

This solution has a time complexity of O(n) where n is the length of the word.

Please note that this solution assumes that the input word contains English letters only. If the input word may contain non-English letters, you should add a check for this in your code.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2Given a string, you have to find out if the string is a valid email or not.A valid email should follow these rules:1. It should have exactly one '@' symbol.2. It should have at least one '.' after the '@'.3. It should not start with '.' or contain consecutive dots.4. It should contain only alphanumeric characters, dots or underscores.5. After the '@', it should contain at least one character before the '.'.6. The domain part of the email should not start or end with a dot.Example:valid emails: "user@example.com","user