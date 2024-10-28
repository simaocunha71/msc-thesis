def differ_At_One_Bit_Pos(a, b):
    # Convert the numbers to binary and remove the '0b' prefix
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]
    
    # Make the binary strings of the same length
    max_len = max(len(bin_a), len(bin_b))
    bin_a = bin_a.zfill(max_len)
    bin_b = bin_b.zfill(max_len)
    
    # Check if the binary strings differ at one position
    for i in range(max_len):
        if bin_a[i] != bin_b[i]:
            # If we find a position where they differ
            # Check if there are any more positions where they differ
            for j in range(i+1, max_len):
                if bin_a[j] != bin_b[j]:
                    # If we find another position where they differ, return False
                    return False
            return True
    # If we have not returned by now, it means they do not differ at one position
    return False