def sum_average(n):
    sum_of_numbers = n * (n + 1) // 2
    average = sum_of_numbers / n
    return (sum_of_numbers, average)

print(sum_average(10))  # returns (55, 5.5)


"""
