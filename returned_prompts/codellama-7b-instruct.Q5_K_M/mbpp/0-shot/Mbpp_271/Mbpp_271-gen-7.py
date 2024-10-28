def even_Power_Sum(n):
    sum = 0
    for i in range(2, n + 1):
        sum += i ** 5
    return sum

# OR

def even_Power_Sum(n):
    return sum(i**5 for i in range(2,n+1,2))