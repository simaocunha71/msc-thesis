def find_Average_Of_Cube(n):
    sum = 0
    for i in range(n):
        sum = sum + (i**3)
    return sum/n