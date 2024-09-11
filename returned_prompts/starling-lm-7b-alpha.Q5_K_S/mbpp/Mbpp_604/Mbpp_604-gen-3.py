def reverse_words(s):
    s = s.split()
    s.reverse()
    return ' '.join(s)


def test_reverse_words():
    assert reverse_words("python program")==("program python")

test_reverse_words()



"""
def reverse_words(s):
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return " ".join(words)
"""

"""
def reverse_words(s):
    return " ".join(s.split()[::-1])
"""

"""
def reverse_words(s):
    return " ".join(reversed(s.split()))
"""


# Other Solutions
"""
def reverse_words(s):
    words = s.split()
    words.reverse()
    return " ".join(words)
"""
"""
def reverse_words(s):
    return " ".join(reversed(s.split()))
"""

"""
def reverse_words(s):
    return " ".join(s.split()[::-1])
"""
"""
def reverse_words(s):
    return " ".join(reversed(s.split()))
"""
"""
def reverse_words(s):
    return " ".join(s.split()[::-1])
"""

"""
def reverse_words(s):
    return " ".join(reversed(s.split()))
"""

"""
def reverse_words(s):
    s = s.split()
    s.reverse()
    return ' '.join(s)
"""
"""
def reverse_words(s):
    return " ".join(s.split()[::-1])
"""
"""
def reverse_words(s):
    return " ".join(reversed(s.split()))
"""

"""
def reverse_words(s):
    return " ".join(reversed(s.split()))
"""

"""
def reverse_words(s):
    return " ".join(s.split()[::-1])
"""

"""
def reverse_words(s):