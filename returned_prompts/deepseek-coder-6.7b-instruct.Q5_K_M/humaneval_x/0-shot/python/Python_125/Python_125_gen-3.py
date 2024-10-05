
def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum(1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 == 1)

print(split_words("Hello world!"))  # ➞  ["Hello", "world!"]
print(split_words("Hello,world!"))  # ➞  ["Hello", "world!"]
print(split_words("abcdef"))  # ➞ 3

This solution works by first checking if there are any whitespace characters in the string. If there are, it splits the string by these characters. If there are not, it checks for commas and splits the string by these characters, too. If there are neither whitespace nor commas, it counts the number of lower-case letters with odd order in the alphabet.
"""

# Test cases:
assert split_words("Hello worlda") == ["Hello", "worlda"]
assert split_words("Hello,worlda") == ["Hello", "worlda"]
assert split_words("Hello worlda,") == ["Hello", "worlda,"]
assert split_words("abcdef") == 3
assert split_words("abcde") == 0
assert split_words("abcdefghijklmnopqrstuvwxyz") == 13
assert split_words("a,b,c,d,e,f") == ["a", "b", "c", "d", "e", "f"]
assert split_words("a b c d e f") == ["a", "b", "c", "d", "e", "f"]
assert split_words("a,b,c,d,e,f") == ["a", "b", "c", "d", "e", "f"]
assert split_words("Hello worlda,b,c,d,e,f") == ["Hello", "worlda", "b", "c", "d", "e", "f"]
assert split_words("Hello worlda b c d e f") == ["Hello", "worlda",