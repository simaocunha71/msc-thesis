def find_Average_Of_Cube(n):
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    avg_of_cubes = sum_of_cubes / n
    return avg_of_cubes