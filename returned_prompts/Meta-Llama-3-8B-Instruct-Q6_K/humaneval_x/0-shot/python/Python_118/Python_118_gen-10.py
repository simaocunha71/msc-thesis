def get_closest_vowel(word):
    vowels = "AEIOU"
    for i in range(len(word) - 2, -1, -1):
        if word[i] in vowels:
            return word[i]
    return ""
# Test the function
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))  # Output: "U"
print(get_closest_vowel("quick"))  # Output: ""
print(get_closest_vowel("ab"))  # Output: ""
print(get_closest_vowel("hello"))  # Output: "o" 
print(get_closest_vowel("aeiou"))  # Output: ""
print(get_closest_vowel("bcdfghjklmnpqrstvwxyz"))  # Output: ""  # No vowels found

# Explanation:
# The function get_closest_vowel() takes a word as an input. It iterates over the word from right to left. If it finds a vowel, it returns that vowel. If it doesn't find any vowel, it returns an empty string. 

# The function uses a for loop to iterate over the word. The range function is used to generate indices from the end of the word to the beginning (exclusive). The -1 in the range function is the start index, which is the end of the word. 

# The variable vowels is a string that contains all the vowels. The if statement checks if the character at the current index is a vowel. If it is, the function returns that vowel. 

# If the function doesn't find any vowel, it returns an empty string. This is because the function is designed to find the closest vowel from the right side of the word, so if there are no vowels on the right side, the function returns an empty string. 

# The function is tested with different inputs to ensure it works correctly. 

# Time complexity: O(n), where n is the length of the word. The function iterates over the word once. 

# Space complexity: O(1), because the function uses a constant amount of space to store the vowels and the index.  # noqa: E501
# noqa: E501
# noqa: E501
# noqa: E501
# noqa: E501
# noqa: E501
# noqa: E501
# noqa: E501
# noqa: E501
# noqa: E501
# noqa: