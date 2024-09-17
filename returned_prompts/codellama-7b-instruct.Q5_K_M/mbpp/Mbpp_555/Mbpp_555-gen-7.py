
def difference(n):
    sum_cubes = sum([i**3 for i in range(n+1)])
    sum_numbers = sum(range(n+1))
    return sum_cubes - sum_numbers


