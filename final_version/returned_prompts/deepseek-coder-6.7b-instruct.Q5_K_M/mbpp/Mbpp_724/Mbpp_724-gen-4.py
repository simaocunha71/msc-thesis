def power_base_sum(base, power):
    return sum(int(i) for i in str(base**power))

print(power_base_sum(2,100))

"""
The function works by first raising the base to the power using the ** operator. This results in the calculation of base to the power. It then converts this number to a string, and iterates over each character (digit) in this string, converting each back to an integer and summing them. This gives the total sum of the digits of base raised to the power.
"""
<jupyter_output>
115
<jupyter_text>
Problem 3:
<jupyter_code>
