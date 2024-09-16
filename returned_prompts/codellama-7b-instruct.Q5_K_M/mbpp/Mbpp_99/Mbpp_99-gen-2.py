def decimal_to_binary(n):
    return bin(n)[2:]

# OR

def decimal_to_binary(n):
    return bin(n)[2:].rstrip('0')

# OR

def decimal_to_binary(n):
    return ''.join(str(n % 2) for n in range(n.bit_length()-1, -1, -1))

# OR

def decimal_to_binary(n):
    return bin(n)[2:].zfill(n.bit_length()-1)
