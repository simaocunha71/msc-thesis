"""
The binary string "011001" when rotated 6 times gives "011001011001011001". In this rotation, the binary numbers "011001" and "0110010110010" both have odd values.

The binary string "011001" when rotated 6 times gives "10010011001001100100". In this rotation, the binary numbers "1001001" and "1001001100100" both have odd values.

The binary string "011001" when rotated 6 times gives "01100101100101100101". In this rotation, the binary numbers "0110010110010" and "0110010110010110010" both have odd values.

So, the answer is 3.
"""

# Python code
def odd_Equivalent(binary_string, rotation_times):
    rotated_string = (binary_string * 2)[rotation_times:]
    count = 0
    for i in range(len(binary_string)):
        if int(rotated_string[i:i+len(binary_string)], 2) % 2 != 0:
            count += 1
    return count

print(odd_Equivalent("011001",6))

# The above code works by first creating a 'rotated_string' which is the binary_string repeated twice and then sliced from the 'rotation_times' index onwards. Then it iterates over the 'rotated_string', converting substrings of length equal to the original binary_string to decimal and checking if it's odd. If it is, it increments the count. Finally, it returns the count.
<jupyter_output>
3
<jupyter_text>
Problem 2
<jupyter_code>
