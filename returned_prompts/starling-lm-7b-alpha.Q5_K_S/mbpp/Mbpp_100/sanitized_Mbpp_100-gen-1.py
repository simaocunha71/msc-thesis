def next_smallest_palindrome(n):
    while True:
        s = str(n)
        if s == s[::-1]:
            return n
        n += 1