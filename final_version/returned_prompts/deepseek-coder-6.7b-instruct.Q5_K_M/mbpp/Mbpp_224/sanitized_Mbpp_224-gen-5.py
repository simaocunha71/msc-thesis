def count_Set_Bits(num):
    # convert the number to binary and remove '0b'
    binary_num = bin(num)[2:]
    
    # count the number of 1s in the binary representation
    set_bits = binary_num.count('1')
    
    return set_bits