def cube_Sum(n):
    return sum(i**3 for i in range(2, 2*n, 2))  # sum of cubes of even numbers from 2 to 2n