def reverse_words(s):
    s = s.split(' ')
    s.reverse()
    return ' '.join(s)

reverse_words("python program")==("program python")






"""

"""



















"""
def reverse_words(s):
    s = s.split(' ')
    s.reverse()
    return ' '.join(s)

reverse_words("python program")==("program python")

"""

"""


def reverse_words(s):
    l = []
    for i in s.split(' '):
        l.append(i)
    l.reverse()
    return ' '.join(l)

reverse_words("python program")==("program python")

"""

"""
def reverse_words(s):
    l = []
    for i in s:
        if i == ' ':
            l.append(' ')
        else:
            l.append(i)
    l.reverse()
    return ''.join(l)

reverse_words("python program")==("program python")

"""

"""
def reverse_words(s):
    l = []
    for i in range(len(s)):
        if s[i] == ' ':
            l.append(' ')
        else:
            l.append(s[i])
    l.reverse()
    return ''.join(l)

reverse_words("python program")==("program python")

"""

"""
def reverse_words(s):
    l = []
    for i in range(len(s)):
        if s[i] == ' ':
            l.append(' ')
        else:
            l.append(s[i])
    l.reverse()
    return ''.join(l)

reverse_words("python program")==("program python")

"""

"""
def reverse_words(s):
    l = []
    for i in range(len(s)):
        if s[i] != ' ':
            l.append(s[i])
        else:
