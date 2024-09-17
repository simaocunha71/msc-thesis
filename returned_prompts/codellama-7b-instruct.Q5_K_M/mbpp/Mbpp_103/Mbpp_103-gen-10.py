
def eulerian_num(n: int, m: int) -> int:
    if n == 1:
        return 1
    if m == 1:
        return n
    return (n * eulerian_num(n - 1, m - 1)) + eulerian_num(n - 1, m)


