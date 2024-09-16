def find_Average_Of_Cube(n):
    list_of_numbers = [i**3 for i in range(1,n+1)]
    sum = 0
    for num in list_of_numbers:
        sum += num
    return sum/(n*(n+1))/(2*n+1)