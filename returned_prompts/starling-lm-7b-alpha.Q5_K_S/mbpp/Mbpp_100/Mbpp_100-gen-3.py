
def next_smallest_palindrome(n: int) -> int:
    if str(n) == str(n)[::-1]:
        return n + 1
    else:
        while True:
            if str(n) == str(n)[::-1]:
                return n
            else:
                n += 1


