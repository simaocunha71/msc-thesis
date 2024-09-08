def power_base_sum(base, power):
    return sum(map(int, str(base ** power)))

print(power_base_sum(2, 100))  # Output: 115

Explanation:
The function first calculates the result of raising the base to the power. The result is converted to a string, and then each character is converted back to an integer before being summed. The sum is returned as the result.
"""
