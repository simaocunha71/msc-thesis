def square_Sum(n):
    sum = 0
    num = 1
    for i in range(n):
        sum += num * num
        num += 2
    return sum