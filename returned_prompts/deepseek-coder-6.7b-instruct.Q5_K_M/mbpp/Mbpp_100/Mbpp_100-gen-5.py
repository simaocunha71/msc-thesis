
def next_smallest_palindrome(n):
    if str(n) == str(n)[::-1]:
        return n
    else:
        return next_smallest_palindrome(n+1)


