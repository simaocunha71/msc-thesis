"""
def next_smallest_palindrome(x):
    y = str(x)
    if y == y[::-1]:
        return int(y[:-1])+1
    else:
        return int(y[1:])+1
"""
