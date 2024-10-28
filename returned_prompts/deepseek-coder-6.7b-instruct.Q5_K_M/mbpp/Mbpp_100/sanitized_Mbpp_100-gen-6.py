def next_smallest_palindrome(n):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    n = n + 1
    while not is_palindrome(n):
        n = n + 1
    return n