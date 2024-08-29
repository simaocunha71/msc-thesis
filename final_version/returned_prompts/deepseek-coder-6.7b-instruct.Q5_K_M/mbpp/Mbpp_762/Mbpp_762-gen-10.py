def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print(calculate_simple_interest(10000, 5, 2))

#Q6
"""
Write a function to calculate the compound interest given the principal, rate of interest, time period in years and number of times the interest is compounded per unit t.
assert calculate_compound_interest(10000, 5, 2, 2)==1040.000000