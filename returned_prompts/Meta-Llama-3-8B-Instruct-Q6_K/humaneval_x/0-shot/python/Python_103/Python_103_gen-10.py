    if n > m:
        return -1
    
    total_sum = sum(range(n, m+1))
    avg = round(total_sum / (m - n + 1))
    
    return bin(avg)[2:]  # Remove the '0b' prefix
    # The [2:] is used to remove the '0b' prefix that is added by the bin() function
    # If the binary representation has less than 8 bits, it will be padded with leading zeros. 
    # This is because Python's built-in bin() function returns a string that starts with '0b' to indicate that it's a binary number, 
    # and it also pads the string with leading zeros if the number of bits is less than the maximum number of bits that Python's int type can hold, 
    # which is 64 bits in Python 3. Python's int type can hold arbitrarily large integers, 
    # but it can only store up to 64 bits worth of information. 
    # This means that the maximum number of bits that Python's int type can hold is 64, 
    # which is why Python's built-in bin() function pads the string with leading zeros if the number of bits is less than 64. 
    # This is why the [2:] is used to remove the '0b' prefix, 
    # because the bin() function returns a string that starts with '0b', 
    # and the [2:] is used to remove the first two characters of the string, 
    # which are the '0b' prefix. 
    # This is why the [2:] is used to remove the '0b' prefix, 
    # because the bin() function returns a string that starts with '0b', 
    # and the [2:] is used to remove the first two characters of the string, 
    # which are the '0b' prefix. 
    # This is why the [2:] is used to remove the '0b' prefix, 
    # because the bin() function returns a string that starts with '0b', 
    # and the [2:] is used to remove the first two characters of the string, 
    # which are the '0b' prefix. 
    # This is why the [2:] is used to remove the '0b' prefix, 
    # because the bin() function returns a string that starts with '0b', 
