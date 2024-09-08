def even_binomial_Coeff_Sum(n):
    # Initialize the sum to 0
    sum = 0
    # Loop through all possible values of k from 0 to n
    for k in range(n + 1):
        # If k is even, add the binomial coefficient to the sum
        if k % 2 == 0:
            sum += binomial_coefficient(n, k)
    return sum
def binomial_coefficient(n, k):
    # Calculate the factorial of n and k
    factorial_n = factorial(n)
    factorial_k = factorial(k)
    factorial_n_k = factorial(n - k)
    # Return the binomial coefficient
    return factorial_n // (factorial_k * factorial_n_k)
def factorial(n):
    # If n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Otherwise, calculate the factorial
    else:
        return n * factorial(n - 1)