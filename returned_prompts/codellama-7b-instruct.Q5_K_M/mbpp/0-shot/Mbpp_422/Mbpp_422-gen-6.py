def find_Average_Of_Cube(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**3
    return sum/(n**3)

