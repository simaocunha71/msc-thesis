def next_smallest_palindrome(n):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    if is_palindrome(n):
        return n + 1

    while not is_palindrome(n):
        n -= 1

    return n