def eulerian_num(n: int, m: int) -> int:
    return math.comb(n+m-1, m)