def decimal_to_binary(n):
    return bin(n)[2:]
    # The [2:] is used to remove the '0b' prefix that Python adds to the binary representation. 
    # The bin() function returns a string that starts with '0b', so we use slicing to remove the first two characters. 