"""
def even_binomial_Coeff_Sum(n):
    # Initialize sum
    sum = 0
    # Initialize binomial coefficient
    binom = 1
    # Loop through all even indices in range 0 to n
    for i in range(0, n, 2):
        # Add coefficient to sum
        sum += binom
        # Compute next coefficient
        binom = (binom * (n - i) * (i + 1)) // (i + 1)
    # Return sum
    return sum
"""

# Explanation:
# This function calculates the sum of even index binomial coefficients.
# The binomial coefficient is calculated using the formula:
# binom = (binom * (n - i) * (i + 1)) // (i + 1)
# The function loops through all even indices in the range 0 to n, and adds the coefficient to the sum.
# The result is returned as the sum of the even index binomial coefficients.

# Test Case:
# assert even_binomial_Coeff_Sum(4) == 8
# This test case is checking if the function correctly calculates the sum of even index binomial coefficients for the input 4, which should be 8.

# Complexity:
# The time complexity of this function is O(n) because it loops through all even indices in the range 0 to n.
# The space complexity is O(1) because it only uses a constant amount of additional space to store the sum and binomial coefficient.

# Running Time:
# The running time of this function is dependent on the value of n.
# For small values of n, the function will run quickly.
# For large values of n, the function may take longer to run because it loops through all even indices in the range 0 to n.

# Testing:
# The function can be tested by providing different values for n and checking if the output matches the expected result.
# Some test cases are provided in the explanation above, but additional test cases can be created to further verify the correctness of the function.

# Optimization:
# The function can be optimized by using a more efficient algorithm to calculate the binomial