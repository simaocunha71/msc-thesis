def differ_At_One_Bit_Pos(a, b):
    # Convert to binary
    a_bin = bin(a)
    b_bin = bin(b)

    # Find the position of the differing bit
    a_bin = a_bin[2:]
    b_bin = b_bin[2:]
    pos = 0
    for i in range(len(a_bin)):
        if a_bin[i] != b_bin[i]:
            break
        pos += 1
    else:
        return False

    # Check if the differing bit is the only differing bit
    for i in range(pos):
        if a_bin[i] != b_bin[i]:
            return False
    for i in range(pos+1, len(a_bin)):
        if a_bin[i] != b_bin[i]:
            return False
    return True
