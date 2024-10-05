
def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum(1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 != 0)

print(split_words("Hello world!"))  # ➞ ["Hello", "world!"]
print(split_words("Hello,world!"))  # ➞ ["Hello", "world!"]
print(split_words("abcdef"))  # ➞ 3


# In the third example, only 'b', 'd' and 'f' are lowercase letters with odd order in the alphabet so the result is 3.


# Notes:
# The ord() function returns an integer representing the Unicode character.
# The % operator returns the remainder of the division. So, (ord(c) - ord('a')) % 2 != 0 is True if the character c is a lowercase letter with an odd order in the alphabet, and False otherwise.
# The sum() function returns the sum of all items in an iterable. The 1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 != 0 part of the sum is 1 for each lowercase letter with odd order in the alphabet, and 0 for each other character, so the sum is the total number of lowercase letters with odd order in the alphabet.
# The split() function splits a string into a list of words. The argument to split() is the delimiter, which is a space character in this case.
# The islower() method returns True if all the case-based characters (letters) of the string are lowercase, otherwise False.
<jupyter_output>
['Hello', 'worlds']
['Hello', 'worlds']
3
<jupyter_text>
Q2:
<jupyter_code>
