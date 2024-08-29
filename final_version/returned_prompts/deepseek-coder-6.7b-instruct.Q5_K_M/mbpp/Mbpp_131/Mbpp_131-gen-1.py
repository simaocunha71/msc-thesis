
def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    s = list(s)
    i, j = 0, len(s) - 1

    while i < j:
        if s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    return ''.join(s)

print(reverse_vowels("Python")) # "Pythn"

"""
Explanation:

The function reverse_vowels accepts a string s and finds the vowels by checking if each character in the string is in the string "aeiouAEIOU". 
If it is, it adds it to the vowels list. Then it creates two pointers, one at the beginning of the string and one at the end. 
It then enters a while loop that continues until the two pointers meet. If the character at the pointer i is not a vowel, it increments i. 
If the character at the pointer j is not a vowel, it decrements j. If both characters are vowels, it swaps them and increments i and decrements j. 
Finally, it returns the string with the vowels reversed.
"""

# Test Cases
assert reverse_vowels("Hello") == "Hollo"
assert reverse_vowels("Python") == "Pythn"
assert reverse_vowels("Javascript") == "Javascrpt"
assert reverse_vowels("") == ""
assert reverse_vowels("aeiou") == "uoiea"
assert reverse_vowels("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"
assert reverse_vowels("AEIOU") == "UOIEA"
assert reverse_vowels("1234567890") == "1234567890"
assert reverse_v