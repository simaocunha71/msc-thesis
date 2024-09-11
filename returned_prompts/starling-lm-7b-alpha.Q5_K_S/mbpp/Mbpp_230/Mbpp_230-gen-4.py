def replace_blank(s, c):
    return s.replace(' ', c)

# assert replace_blank("hello people",'@')==("hello@people")
# print(replace_blank("hello people",'@'))


# def replace_blank(s, c):
#     i = 0
#     while i < len(s):
#         if s[i] == " ":
#             s = s[:i] + c + s[i+1:]
#         i += 1
#     return s

# assert replace_blank("hello people",'@')==("hello@people")
# print(replace_blank("hello people",'@'))


def replace_blank(s, c):
    while ' ' in s:
        s = s.replace(' ', c)
    return s

# assert replace_blank("hello people",'@')==("hello@people")
# print(replace_blank("hello people",'@'))


def replace_blank(s, c):
    return s.translate(str.maketrans(' ', c))

# assert replace_blank("hello people",'@')==("hello@people")
# print(replace_blank("hello people",'@'))


def replace_blank(s, c):
    for x in s:
        if x == ' ':
            s = s.replace(' ', c)
    return s

# assert replace_blank("hello people",'@')==("hello@people")
# print(replace_blank("hello people",'@'))


def replace_blank(s, c):
    return s.translate(str.maketrans(None, c))

# assert replace_blank("hello people",'@')==("hello@people")
# print(replace_blank("hello people",'@'))


def replace_blank(s, c):
    for i in range(len(s)):
        if s[i] == ' ':
            s = s[:i] + c + s[i+1:]
    return s

# assert replace_blank("hello people",'@')==("hello@people")
# print(replace