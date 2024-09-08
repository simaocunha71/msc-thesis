
def power_base_sum(base, power):
    return sum(int(i) for i in str(base ** power))

print(power_base_sum(2,100))

"""
Output:
115
"""

Explanation:
The function first calculates the base to the power of the given power. It then converts this number into a string and iterates through each digit, converting each back into an integer and adding them together.

"""

