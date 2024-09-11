def even_Power_Sum(n):
    return sum(i**5 for i in range(2, 2*n, 2))  # 2*n is used because we need to go up to 2*n for n even numbers