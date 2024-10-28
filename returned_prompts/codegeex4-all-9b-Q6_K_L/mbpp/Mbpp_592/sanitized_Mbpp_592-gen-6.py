def sum_Of_product(n):
    sum = 0
    for i in range(n):
        sum += (i+1)*(i+2)//2
    return sum