def differ_At_One_Bit_Pos(a, b):
    # Convert the integers to binary and remove the '0b' prefix
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]
    
    # Check if the lengths of the binary strings are different
    if len(bin_a) != len(bin_b):
        return False
    
    # Initialize a counter for the different bits
    diff_count = 0
    
    # Iterate over the binary strings
    for i in range(len(bin_a)):
        # Check if the bits at the current position are different
        if bin_a[i] != bin_b[i]:
            diff_count += 1
            
            # If more than one different bit is found, return False
            if diff_count > 1:
                return False
            
    # If exactly one different bit is found, return True
    return diff_count == 1