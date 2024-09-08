def count_Set_Bits(n):
    binary = bin(n)[2:] # Convert to binary and remove the '0b' prefix
    set_bits = [bit for bit in binary if bit == '1'] # List comprehension to find the set bits
    return len(set_bits) # Return the count of set bits