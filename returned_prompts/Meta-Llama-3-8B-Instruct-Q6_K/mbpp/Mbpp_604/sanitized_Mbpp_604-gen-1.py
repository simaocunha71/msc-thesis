def reverse_words(s):
    return ' '.join(s.split()[::-1])  # using slicing to reverse the list of words, then join them back together with spaces
    # or
    return ' '.join(reversed(s.split()))  # using the reversed function to reverse the list of words, then join them back together with spaces