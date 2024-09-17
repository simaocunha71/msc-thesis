def tetrahedral_number(n: int) -> int:
    n = n + 1
    return n * (n * n + 1) // 2