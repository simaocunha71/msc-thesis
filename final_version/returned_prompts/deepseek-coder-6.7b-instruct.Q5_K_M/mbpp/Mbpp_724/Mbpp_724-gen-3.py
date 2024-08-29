def power_base_sum(base, power):
    return sum(map(int, str(base ** power)))

print(power_base_sum(2, 100))

Explanation:
The function power_base_sum first calculates the result of base to the power of power. It then converts this result to a string and maps the int function to this string, effectively converting each digit of the number to an integer. This resulting iterable is then passed to the sum function to calculate the total sum of all the digits in the number.
"""

