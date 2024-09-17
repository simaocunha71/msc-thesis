from string import ascii_lowercase
def find_char_long(s):
    return [x for x in s.split() if len(x)>=4]