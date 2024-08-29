def power_base_sum(base, power):
    return sum(int(i) for i in str(base ** power))

print(power_base_sum(2,100)) # Output: 115

Explanation:

In this problem, we first calculate the result of the base raised to the power. Then we convert this result to a string so we can iterate over the digits. After that, we convert each digit back to an integer and sum them up.
"""

# Test cases
assert power_base_sum(2,100)==115
assert power_base_sum(3,50)==25
assert power_base_sum(5,50)==25
assert power_base_sum(10,100)==101
assert power_base_sum(20,200)==210
assert power_base_sum(2,1000)==1151
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 10:
<jupyter_code>
"""
