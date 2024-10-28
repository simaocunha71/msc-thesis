def reverse_words(s):
    return ' '.join(s.split()[::-1])  # split by space, reverse the list and join with space