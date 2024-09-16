def next_Perfect_Square(num):
    # Initialize a variable to store the next perfect square
    next_perfect_square = num
 
    # Loop through all the numbers from num+1 to infinity
    for i in range(num + 1, 10000000000):
        # Check if the number is a perfect square
        root = i ** 0.5
        if root == int(root):
            # If yes, then return the number
            next_perfect_square = i
            break
    return next_perfect_square