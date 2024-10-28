
import re

def reverse_delete(s, c):
    s = re.sub('[' + c + ']', '', s)
    return (s, s == s[::-1])
