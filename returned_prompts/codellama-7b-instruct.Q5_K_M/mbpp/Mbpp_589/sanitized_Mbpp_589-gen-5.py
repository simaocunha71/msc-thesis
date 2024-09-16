def perfect_squares(n1, n2):
    # Initialize an empty list to store the perfect squares
    perfect_squares_list = []
    # Iterate from n1 to n2
    for num in range(n1, n2+1):
        # Check if the number is a perfect square
        root = num ** 0.5
        # If the number is a perfect square, append it to the list
        if root == int(root):
            perfect_squares_list.append(num)
    # Return the list of perfect squares
    return perfect_squares_list