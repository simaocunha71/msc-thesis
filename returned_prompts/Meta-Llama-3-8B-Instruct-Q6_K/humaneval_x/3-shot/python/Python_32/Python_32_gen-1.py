    # Check if the list has an even number of coefficients
    if len(xs) % 2 != 0:
        raise ValueError("xs must have even number of coefficients")

    # Initialize the result
    result = 0.0

    # Loop through the coefficients
    for i, coeff in enumerate(xs):
        # Calculate the term for the current coefficient
        term = coeff * math.pow(result, i)

        # Update the result
        result += term

    # Return the result
    return result


