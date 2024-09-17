def find_Average_Of_Cube(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 1:
        raise ValueError("Input must be a positive integer")
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    return sum_of_cubes / n