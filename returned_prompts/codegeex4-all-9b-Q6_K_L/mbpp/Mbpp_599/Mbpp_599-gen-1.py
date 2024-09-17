def sum_average(n: int) -> tuple:
    total = sum(range(1, n+1))
    average = total / n
    return (total, average)