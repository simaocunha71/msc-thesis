def next_smallest_palindrome(n):
    def is_palindrome(m):
        s = str(m)
        return s == s[::-1]

    while True:
        n += 1
        if is_palindrome(n):
            return n