def next_smallest_palindrome(n):
    if str(n) == str(n)[::-1]:
        return n
    else:
        n = n + 1
        while str(n) != str(n)[::-1]:
            n = n + 1
        return n