def next_smallest_palindrome(n):
    if n < 10: return n + 1
    while True:
        n += 1
        s = str(n)
        if s == s[::-1]: return n