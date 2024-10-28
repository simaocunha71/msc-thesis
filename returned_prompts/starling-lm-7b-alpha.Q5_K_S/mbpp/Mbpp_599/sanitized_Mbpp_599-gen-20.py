def sum_average(n: int) -> (int, float):
    sum_of_n = n * (n + 1) // 2
    average = sum_of_n / n
    return (sum_of_n, average)