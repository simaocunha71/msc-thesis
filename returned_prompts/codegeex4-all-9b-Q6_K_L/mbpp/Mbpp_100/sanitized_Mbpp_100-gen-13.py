def next_smallest_palindrome(n: int) -> int:
    n += 1
    while not str(n) == str(n)[::-1]:
        n += 1
    return n