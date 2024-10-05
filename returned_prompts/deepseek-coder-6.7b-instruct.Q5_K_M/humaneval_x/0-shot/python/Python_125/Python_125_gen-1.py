
def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum(1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 != 0)

print(split_words("Hello world!")) # ➞ ["Hello", "world!"]
print(split_words("Hello,world!")) # ➞ ["Hello", "world!"]
print(split_words("abcdef")) # ➞ 3


'''
Test cases:
1. 'Hello world!' has two words, so we split on the space and get ['Hello', 'world!'].
2. 'Hello,world!' has two words, so we split on the comma and get ['Hello', 'world!'].
3. 'abcdef' has six letters, but we only count lower-case letters with odd order in the alphabet, so we get 3 (a, c, e).
'''


'''
This function works by first checking if there is a space character in the input string. If there is, it splits the string on this character and returns the resulting list. If there is no space, it then checks for a comma. If there is a comma, it splits the string on this character and returns the resulting list. If there are neither spaces nor commas, it counts the number of lower-case letters with odd order in the alphabet and returns this number.
'''


'''
The function uses the built-in string method split() to split the input string on a specified character. The string method islower() is used to check if a character is a lower-case letter, and the built-in function ord() is used to get the Unicode point of a character.
'''


'''
The function uses a generator expression to count the number of lower-case letters with odd order in the alphabet. The expression uses the bitwise operator % to check if the Unicode point of a character minus the Unicode point of 'a' is not divisible by 2.
'''


'''
The function uses the bitwise operator % to check if the Un