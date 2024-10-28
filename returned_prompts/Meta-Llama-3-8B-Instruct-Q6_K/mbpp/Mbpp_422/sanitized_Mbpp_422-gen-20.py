def find_Average_Of_Cube(n):
    sum_cubes = 0
    for i in range(1, n+1):
        sum_cubes += i**3
    return sum_cubes / n