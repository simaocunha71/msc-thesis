def start_withp(words):
    result = []
    for word in words:
        if word.startswith('p'):
            result.append(word)
    if len(result) == 2:
        return result[0], result[1]
    elif len(result) == 1:
        return result[0], ''
    else:
        return '', ''


assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')




"""
Given two strings, return True if the first string contains the same sequence of characters as the second string,
 but in a different order.

For example:

assert is_anagram('listen', 'silent') == True
assert is_anagram('hello', 'world') == False
"""


def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


assert is_anagram('listen', 'silent') == True
assert is_anagram('hello', 'world') == False


"""
Given a string, return True if the string is a palindrome, otherwise return False.

For example:

assert is_palindrome('racecar') == True
assert is_palindrome('hello') == False
"""


def is_palindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


assert is_palindrome('racecar') == True
assert is_palindrome('hello') == False


"""
Given a list of strings, return a new list with all the strings that have the same length.
For example:

assert same_length_words(['Apple', 'Banana', 'Grapes']) == ['Apple', 'Banana']
