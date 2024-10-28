def find_Average_Of_Cube(n):
    """
    Function to find the average of cubes of first n natural numbers.
    """
    total = 0
    for i in range(1, n+1):
        total += i**3
    return total / n