"""
The binary representation of 9 is 1001. 
Toggling bits of 1001 from the 2nd bit to the 3rd bit gives 1101 (13 in decimal).
But, the problem statement requires to toggle bits of the number except the first and the last bit.
So, we need to toggle bits of 1001 from the 2nd bit to the 2nd last bit, which gives us 1100 (12 in decimal).
"""

def toggle_middle_bits(n):
    binary = bin(n)[2:]
    binary = list(binary)
    for i in range(1, len(binary)-1):
        if binary[i] == '1':
            binary[i] = '0'
        else:
            binary[i] = '1'
    return int(''.join(binary), 2)

assert toggle_middle_bits(9) == 12


"""
Explanation:
- First, we convert the number to binary and remove the '0b' prefix that Python adds.
- We then convert the binary string to a list so that we can manipulate individual characters (bits).
- We then iterate over the list from the 2nd character to the 2nd last character (excluding the first and last characters) and toggle each bit.
- We join the list back together into a string and convert it back to an integer.
- Finally, we return the result.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2:
<jupyter_code>
