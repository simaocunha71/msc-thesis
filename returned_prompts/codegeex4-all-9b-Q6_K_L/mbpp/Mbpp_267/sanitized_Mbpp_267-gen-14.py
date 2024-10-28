def square_Sum(n):
    if n%2 == 0:
        n = n-1
    sum = 0
    for i in range(1,n+1,2):
        sum += i**2
    return sum