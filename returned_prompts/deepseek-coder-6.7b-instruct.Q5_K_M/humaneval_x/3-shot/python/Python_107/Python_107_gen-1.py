    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    even_count = 0
    odd_count = 0

    for i in range(1, n + 1):
        if