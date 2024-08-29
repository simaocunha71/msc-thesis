def count_Set_Bits(n):
    count = 0
    while n:
        count += n % 2
        n //= 2
    return count

print(count_Set_Bits(2))


# The function works by taking the modulus of the number by 2 to get the last bit. 
# If the last bit is 1, then it increments the counter. 
# It then performs integer division by 2 to remove the last bit. 
# This process continues until the number becomes 0.
# Finally, it returns the count which is the number of set bits in the binary representation of the input number.
<jupyter_output>
1
<jupyter_text>
Example 2
<jupyter_code>
