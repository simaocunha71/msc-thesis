def find_lucas(n):
    # Initialize the first two terms
    a, b = 2, 1
    # Iterate over the remaining terms
    while n > 0:
        # Calculate the next term
        c = a + b
        # Update the terms
        a, b = b, c
        # Subtract the current term
        n -= 1
    return c