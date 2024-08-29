def reverse_words(s):
    words = s.split()
    words = words[::-1]
    return ' '.join(words)

assert reverse_s("python program")==("program python")
"""
