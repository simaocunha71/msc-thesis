def difference(n):
    sum_of_nums = (n * (n + 1)) / 2
    sum_of_cubes = n * (n + 1) * (2 * n + 1) / 6
    difference = sum_of_cubes - sum_of_nums
    return difference