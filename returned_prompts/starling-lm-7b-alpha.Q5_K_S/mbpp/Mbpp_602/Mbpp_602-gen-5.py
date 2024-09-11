"""
def first_repeated_char(str):
    set_str = set(str)
    for i in range(len(str)):
        if str[i] in set_str and str.count(str[i]) > 1:
            return str[i]


print(first_repeated_char("abcabc"))
"""

def first_repeated_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

print(first_repeated_char("abcabc"))


def first_repeated_char(s):
    for char in s:
        if s.count(char) > 1:
            return char
    return None

print(first_repeated_char("abcabc"))

def first_repeated_char(s):
    for i in range(len(s)):
        if s.count(s[i]) > 1:
            return s[i]
    return None

print(first_repeated_char("abcabc"))

def first_repeated_char(s):
    count_dict = {}
    for char in s:
        if char in count_dict:
            return char
        else:
            count_dict[char] = 1
    return None

print(first_repeated_char("abcabc"))

def first_repeated_char(s):
    count_dict = {}
    for i in range(len(s)):
        if s[i] in count_dict:
            return s[i]
        else:
            count_dict[s[i]] = 1
    return None

print(first_repeated_char("abcabc"))

def first_repeated_char(s):
    count_dict = {}
    for i in range(len(s)):
        if s[i] in count_dict:
            return s[i]
        else:
            count_dict[s[i]] = 1
    return None

print(first_repeated_char("abcabc"))


def first_repeated_char(