def difference(n):
    sum_cubes = sum(i**3 for i in range(1, n+1))
    sum_numbers = (n*(n+1))/2
    return sum_cubes - sum_numbers