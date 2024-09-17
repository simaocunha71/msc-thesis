def difference(n):
    sum_of_squares = sum(i**2 for i in range(1, n+1))
    sum_of_numbers = sum(range(1, n+1))
    return sum_of_squares**2 - sum_of_numbers**3