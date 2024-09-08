def next_smallest_palindrome(n):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    while True:
        n += 1
        if is_palindrome(n):
            return n