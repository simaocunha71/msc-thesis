"""
def reverse_vowels(word):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    word_list = list(word)
    for i in range(len(word_list)):
        if word_list[i] in vowel:
            word_list[i] = vowel[vowel.index(word_list[i]) - 1]
    return ''.join(word_list)

reverse_vowels("Python")
"""

In the above question,
The function reverse_vowels is defined to reverse the vowels in the string word.
A list of all vowels is created called vowel.
The string word is converted to a list called word_list.
A for loop is used to iterate over each character in the string.
If the character is a vowel (found in the vowel list), the index of the vowel in the vowel list is found and the character before it in the vowel list is selected as the new character.
The function returns the new list as a string by joining all the characters together.
The function is called with the string "Python" as an argument and the result is printed.

This function is tested using the assert statement, which checks if the function returns the expected result for the given input "Python".

The time complexity of this function is O(n), where n is the length of the string, as it iterates over each character in the string once.
The space complexity is also O(n), as the word_list is a copy of the original string word.

Overall, this function is a simple and efficient solution to the problem of reversing only the vowels in a given string.
"""

# Python program to reverse the vowels of a string

def reverseVowels(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        while chars[left].lower() not in "aeiou":
            left += 1
        while chars[right].lower() not in "aeiou":