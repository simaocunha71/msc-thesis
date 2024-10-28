
def next_smallest_palindrome(n: int) -> int:
    while True:
        if str(n) == str(n)[::-1]:
            return n
        n += 1


