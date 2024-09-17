def sum_Of_product(n):
    sum = 0
    for i in range(1,n+1):
        sum += math.factorial(n)/(math.factorial(i)*math.factorial(n-i))
    return sum

