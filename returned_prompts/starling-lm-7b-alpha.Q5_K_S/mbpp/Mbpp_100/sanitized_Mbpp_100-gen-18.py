def next_smallest_palindrome(n):
    if n % 9 == 0:
        return 9 * (n // 9)
    else:
        return 9 * (n // 9 + 1) + (n % 9 + 1) - 1