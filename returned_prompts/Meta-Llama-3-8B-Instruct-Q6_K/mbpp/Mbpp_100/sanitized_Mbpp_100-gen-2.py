def next_smallest_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n
def is_palindrome(n):
    return str(n) == str(n)[::-1]  # convert to str and check if it's equal to its reverse