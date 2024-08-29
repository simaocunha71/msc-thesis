
def odd_Equivalent(binary,rotations):
    odd_count = 0
    binary = binary * rotations
    for i in range(rotations):
        rotated_binary = binary[i:] + binary[:i]
        if int(rotated_binary,2) % 2 == 1:
            odd_count += 1
    return odd_count

print(odd_Equivalent("011001",6)) # 3
"""
Explanation:
- The binary string "011001" is rotated 6 times to get 6 different rotations:
  "011001", "100101", "110010", "011001", "001101", "100101".
- The decimal equivalent of each of these binary strings is 1, 5, 6, 1, 5, 5.
- Of these, only 1, 5, and 5 are odd numbers, so the function returns 3.
"""


"""
The logic used here is that when a binary string is rotated, the decimal equivalent changes by a value which is the sum of the index of rotation and the binary equivalent.
So, if the binary string is rotated and the sum of the index of rotation and the binary equivalent is odd, it means that the decimal equivalent is odd.

The function counts the number of times this happens and returns that count.
"""
<jupyter_output>
3
<jupyter_text>
Question 2
<jupyter_code>
