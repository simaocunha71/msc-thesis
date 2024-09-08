def square_Sum(n):
    # Calculate the first n odd numbers
    odd_numbers = [2*i + 1 for i in range(n)]
    # Calculate the sum of their squares
    return sum([x**2 for x in odd_numbers])