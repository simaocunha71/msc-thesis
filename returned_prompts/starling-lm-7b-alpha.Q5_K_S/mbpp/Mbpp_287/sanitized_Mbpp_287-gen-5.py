def square_Sum(n):
    # Initialize the sum
    sum = 0
    # Loop through the range and add the square of each number
    for i in range(1, n+1):
        sum += i**2
    return sum