"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""
def count_char_position(s):
    c = dict((ord('a'),1), (ord('z'),25))
    result = ""
    for i in s:
        position = ord(i) - ord('a') + 1
        if position in c.keys():
            result += str(position)+" "
            
    return result[1:]
