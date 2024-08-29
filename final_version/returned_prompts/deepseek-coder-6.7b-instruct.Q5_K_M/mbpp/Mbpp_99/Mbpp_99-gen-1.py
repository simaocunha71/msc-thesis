def decimal_to_binary(n):
    return bin(n)[2:]

print(decimal_to_binary(8))

"""
Explanation:
The 'bin' function in python converts a decimal number into binary. The output will be in the form of a string with '0b' as prefix. So, we use array slicing [2:] to remove the '0b' from the output.
"""
<jupyter_output>
1000
<jupyter_text>
Question 2
<jupyter_code>
