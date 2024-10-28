def even_Power_Sum(n):
    # Initialize the sum to 0
    sum = 0
    # Iterate through the first n even numbers
    for i in range(2, 2 * n + 1, 2):
        # Add the square of each number to the sum
        sum += i ** 5
    # Return the sum
    return sum