    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    even_count = 0
    odd_count = 0
    for i in range(1, n+1):
        if is_palindrome(i) and i % 2 == 0:
            even_count += 1
        if is_palindrome(i) and i % 2 != 0:
            odd_count += 1
    return even_count, odd_count


