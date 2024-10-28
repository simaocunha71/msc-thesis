def bell_number(n):
    # Initialize a table to store the results of sub-calculations
    B = [0]*(n+1)
    B[0] = 1
    B[1] = 1

    # Create a table to store the results of sub-calculations
    C = [0]*(n+1)
    C[0] = 1
    C[1] = 1

    # Compute the Bell numbers
    for i in range(2, n+1):
        B[i] = C[i-1] + sum(C[j]*B[i-j-1] for j in range(i-1))
        C[i] = sum(C[j]*B[i-j-1] for j in range(i))

    return B[n]