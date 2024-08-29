def toggle_middle_bits(n):
    binary = bin(n)[2:]
    middle_bits = list(binary[1:-1])
    for i in range(len(middle_bits)):
        middle_bits[i] = '1' if middle_bits[i] == '0' else '0'
    return int(binary[0] + ''.join(middle_bits) + binary[-1], 2)

assert toggle_middle_bits(9) == 15
"""
Explanation:
Binary representation of 9 is 1001. If we toggle bits of the number except the first and the last bit, we get 1111, which is the decimal equivalent of 15.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
