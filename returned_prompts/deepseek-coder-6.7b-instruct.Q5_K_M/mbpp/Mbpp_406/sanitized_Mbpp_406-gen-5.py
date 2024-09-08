def find_Parity(num):
    """
    This function takes an integer as input and returns True if the parity (number of 1s in binary representation) of the 
    given number is odd, else it returns False.
    """
    binary_num = bin(num)[2:] # binary representation of num
    ones_count = binary_num.count('1') # count of 1s in binary_num
    return ones_count % 2 != 0 # returns True if ones_count is odd else False