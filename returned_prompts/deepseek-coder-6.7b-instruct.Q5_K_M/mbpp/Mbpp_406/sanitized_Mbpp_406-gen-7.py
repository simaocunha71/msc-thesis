def find_Parity(n):
    # convert the number to binary
    bin_n = bin(n)[2:]
    # count the number of ones in the binary representation
    count = bin_n.count('1')
    # if count is odd, return True, else return False
    return count % 2 != 0