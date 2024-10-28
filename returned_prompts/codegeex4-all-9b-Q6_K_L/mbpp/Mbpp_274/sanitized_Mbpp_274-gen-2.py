def even_binomial_Coeff_Sum(n):
    # Initialize the binomial coefficient array
    binomial_coeff = [[0 for i in range(n+1)] for j in range(n+1)]
    
    # Calculate the binomial coefficients
    for i in range(n+1):
        for j in range(i+1):
            if j == 0 or j == i:
                binomial_coeff[i][j] = 1
            else:
                binomial_coeff[i][j] = binomial_coeff[i-1][j-1] + binomial_coeff[i-1][j]
    
    # Calculate the sum of even index binomial coefficients
    even_sum = 0
    for i in range(1, n+1):
        even_sum += binomial_coeff[i][i]
    
    return even_sum