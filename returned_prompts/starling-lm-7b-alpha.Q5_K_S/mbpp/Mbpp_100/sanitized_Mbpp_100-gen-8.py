def next_smallest_palindrome(n):
    if n < 10:
        return n + 1
    if n % 2 == 0:
        return 1 + 10 * (n // 2)
    for i in range(n, 10**(len(str(n))-1), -1):
        if str(i) == str(i)[::-1]:
            return i