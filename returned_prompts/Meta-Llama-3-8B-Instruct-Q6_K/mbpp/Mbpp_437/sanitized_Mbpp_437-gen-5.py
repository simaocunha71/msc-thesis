def remove_odd(s):
    return ''.join(char for i, char in enumerate(s) if i % 2 == 0)  # or use list comprehension