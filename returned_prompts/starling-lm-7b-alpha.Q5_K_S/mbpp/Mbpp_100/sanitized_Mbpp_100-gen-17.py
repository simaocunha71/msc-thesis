def next_smallest_palindrome(n: int) -> int:
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            return n