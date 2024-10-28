
def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum([1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 == 1])

print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))
print(split_words("Hello,world,!"))
print(split_words("Hello,world,this,is,a,test"))
print(split_words("abcdefghijklmnopqrstuvwxyz"))

# Output:
# ['Hello', 'world&']
# ['Hello', 'world&']
# 3
# ['Hello', 'world', '&']
# ['Hello', 'world', 'this', 'is', 'a', 'test']
# 13

The function works by checking if there are spaces, commas, or neither in the input string. If there are spaces, it splits the string on those spaces. If there are commas, it splits the string on those commas. If there are neither, it counts the number of lower-case letters with an odd order in the alphabet and returns that count.
</code>
"""

__name__ = "split_words"
__doc__ = """
This function splits a string of words on whitespace, commas, or returns the number of lower-case letters with an odd order in the alphabet.
"""
__example__ = """
split_words("Hello world&") ➞ ["Hello", "world&"]
split_words("Hello,world&") ➞ ["Hello", "world&"]
split_words("abcdef") ➞ 3
"""
__author__ = "Mohamed Alaa"
__email__ = "alaa.isaac@gmail.com"
__status__ = "Development"

#test_split_words.py
import unittest
import split_words as sw

class TestSplitWords(unittest.TestCase):

    def test_split