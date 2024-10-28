def next_smallest_palindrome(n):
    n += 1
    while not is_palindrome(str(n)):
        n += 1
    return n
def is_palindrome(s):
    return s == s[::-1]