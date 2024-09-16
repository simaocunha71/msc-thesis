def next_smallest_palindrome(n):
    n = str(n)
    n = n[::-1]
    if int(n) < n:
        return int(n)
    else:
        return int(str(int(n) + 1)[::-1])