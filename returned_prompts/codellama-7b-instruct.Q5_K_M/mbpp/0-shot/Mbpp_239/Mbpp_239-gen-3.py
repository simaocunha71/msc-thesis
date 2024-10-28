"""
The number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m, can be calculated using the following formula:

(m^(n+1) - 1) / (m-1)

Here's some sample Python code that demonstrates the formula:

def get_total_number_of_sequences(m, n):
    return (m ** (n+1) - 1) // (m-1)
"""
