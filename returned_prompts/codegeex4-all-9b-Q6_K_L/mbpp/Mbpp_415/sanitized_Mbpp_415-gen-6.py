def max_Product(arr):
    # Initialize variables to store the highest product and the pair of indices
    highest_product = float('-inf')
    pair_indices = None

    # Iterate through all possible pairs of indices
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            # Calculate the product of the current pair
            product = arr[i] * arr[j]
            # Update the highest product and pair indices if necessary
            if product > highest_product:
                highest_product = product
                pair_indices = (i, j)

    # Return the pair of indices with the highest product
    return pair_indices