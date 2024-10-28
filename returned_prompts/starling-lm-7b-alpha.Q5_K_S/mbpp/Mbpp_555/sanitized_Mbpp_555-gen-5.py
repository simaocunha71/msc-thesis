def difference(n):
    # Sum of the first n natural numbers
    sum_natural = n * (n + 1) // 2
    # Sum of cubes of the first n natural numbers
    sum_cubes = (n ** 3) * (n + 1) // 2
    # Difference between the two sums
    return sum_cubes - sum_natural