
def decimal_to_binary(num):
    bin_str = bin(num)[2:]
    return bin_str.zfill(len(bin(num)[2:]))


