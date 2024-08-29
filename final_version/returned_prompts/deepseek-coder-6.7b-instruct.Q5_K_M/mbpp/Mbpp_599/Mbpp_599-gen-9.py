def sum_average(n):
    sum_n = (n * (n + 1)) // 2
    avg_n = sum_n / n
    return (sum_n, avg_n)

assert sum_average(10)==(55, 5.5)

"""
