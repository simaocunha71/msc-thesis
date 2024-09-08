def toggle_middle_bits(n):
    bin_num = bin(n)[2:]
    bin_num = list(bin_num)
    for i in range(1, len(bin_num)-1):
        if bin_num[i] == '1':
            bin_num[i] = '0'
        else:
            bin_num[i] = '1'
    return int(''.join(bin_num), 2)

print(toggle_middle_bits(9))

# Output: 15

# The function works by first converting the number to binary, then turning the string into a list so that we can manipulate individual bits.
# It then iterates through the bits (skipping the first and last), toggling the bits (changing '1' to '0' and vice versa) and converts the list back to a string, then back to an integer.
<jupyter_output>
15
<jupyter_text>
Question 2:
<jupyter_code>
