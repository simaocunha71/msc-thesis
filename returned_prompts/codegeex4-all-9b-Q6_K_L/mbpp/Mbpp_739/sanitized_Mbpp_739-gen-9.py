def find_Index(n):
    # Calculate the smallest triangular number with n digits
    triangular_number = 10**(n-1)
    # Initialize the index
    index = 1
    # Calculate the triangular number until it has n digits
    while triangular_number < 10**n:
        index += 1
        triangular_number += index
    # Return the index
    return index