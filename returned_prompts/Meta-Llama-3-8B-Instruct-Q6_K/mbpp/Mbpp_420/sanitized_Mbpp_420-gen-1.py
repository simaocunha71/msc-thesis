def cube_Sum(n):
    return sum(i**3 for i in range(2, 2*n+1, 2))  # cube sum of even numbers from 2 to 2n