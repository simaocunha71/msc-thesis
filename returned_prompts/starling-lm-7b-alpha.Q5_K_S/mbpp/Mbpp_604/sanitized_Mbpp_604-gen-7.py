def reverse_words(s):
    s = list(s.split())
    s.reverse()
    return " ".join(s)