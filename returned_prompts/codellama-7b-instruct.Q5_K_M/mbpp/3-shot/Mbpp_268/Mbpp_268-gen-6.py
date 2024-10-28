
def find_star_num(n: int) -> int:
    start = 1
    while n > 0:
        n -= 1
        start += 6 * n
    return start


