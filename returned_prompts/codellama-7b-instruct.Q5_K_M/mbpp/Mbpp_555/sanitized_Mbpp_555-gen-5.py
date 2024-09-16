def difference(n):
    sum_first_n = n * (n + 1) // 2
    sum_cubes = sum([x**3 for x in range(1, n+1)])
    return sum_cubes - sum_first_n