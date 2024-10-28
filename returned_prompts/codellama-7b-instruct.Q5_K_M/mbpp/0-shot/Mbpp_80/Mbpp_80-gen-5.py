def tetrahedral_number(n):
    if n == 0:
        return 0
    return (n * (n + 1)) // 2

print(tetrahedral_number(5)) # 35
