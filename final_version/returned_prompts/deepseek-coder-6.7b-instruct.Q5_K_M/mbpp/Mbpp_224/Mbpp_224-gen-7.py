def count_Set_Bits(n):
    binary = bin(n)[2:] # Convert to binary and remove the '0b' prefix
    set_bits = [bit for bit in binary if bit == '1'] # List comprehension to find the set bits
    return len(set_bits) # Return the count of set bits

print(count_Set_Bits(2)) # Should print 1
"""
Explanation:
2 in binary is '10'. There is one set bit (1).
"""

"""
