def next_smallest_palindrome(n):
    n = str(n)
    while True:
        n = str(int(n) - 1)
        if n == n[::-1]:
            return int(n)