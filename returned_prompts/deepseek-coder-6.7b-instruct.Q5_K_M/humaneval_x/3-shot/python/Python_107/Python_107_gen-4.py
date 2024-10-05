    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    even_count = sum(is_palindrome(i) and i % 2 == 0 for i in range(1, n+1))
    odd_count = sum(is_palindrome(i) and i % 2 == 1 for i in range(1, n+1))

    return (even_count, odd_count)


