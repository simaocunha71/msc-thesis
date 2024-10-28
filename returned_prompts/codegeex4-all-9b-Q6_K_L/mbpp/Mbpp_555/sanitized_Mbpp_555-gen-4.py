def difference(n):
    sum_cubes = n * (n + 1) // 2 * (2 * n + 1) // 3
    sum_numbers = n * (n + 1) // 2
    return sum_cubes - sum_numbers