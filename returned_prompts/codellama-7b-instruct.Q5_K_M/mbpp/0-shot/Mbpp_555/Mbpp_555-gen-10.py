def difference(n):
    sum_cubes = 0
    for i in range(n+1):
        sum_cubes += i**3
    return sum_cubes - (n*(n+1))//2
