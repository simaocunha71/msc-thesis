
def odd_Equivalent(bin_str, rotations):
    odd_count = 0
    bin_str = bin_str * rotations
    for i in range(rotations):
        rotated_str = bin_str[i:len(bin_str) - rotations + i] + bin_str[0:i]
        if int(rotated_str, 2) % 2 != 0:
            odd_count += 1
    return odd_count

print(odd_Equivalent("011001",6))
assert odd_Equivalent("011001",6) == 3

"""
Explanation:

Here, the function takes a binary string and the number of rotations as arguments.
It firstly repeats the binary string by the number of rotations.
Then it generates all possible rotations of the string and converts each rotation into an integer.
If the integer is odd, it increments the counter.
Finally, it returns the counter.
"""
<jupyter_output>
3
<jupyter_text>
Question 2
<jupyter_code>
"""
