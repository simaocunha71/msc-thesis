def even_Power_Sum(n: int) -> int:
    sum_of_evens = 0
    for i in range(2, 2*n+1, 2):
        sum_of_evens += i**5
    return sum_of_evens