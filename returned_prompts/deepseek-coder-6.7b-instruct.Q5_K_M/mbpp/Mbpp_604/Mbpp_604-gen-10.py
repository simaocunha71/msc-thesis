def reverse_words(s: str):
    return ' '.join(s.split()[::-1])

assert reverse_words("python program")==("program python")

"""
The function works by splitting the string into a list of words using the split() function. The [::-1] part reverses the list. Finally, the ' '.join(list) part combines the words back into a single string with spaces between them.
"""

# Task 2

