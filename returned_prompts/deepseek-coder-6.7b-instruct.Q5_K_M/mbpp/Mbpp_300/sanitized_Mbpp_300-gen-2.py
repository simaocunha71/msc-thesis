def count_binary_seq(n):
    # initialize the count to 0
    count = 0
    # iterate from 0 to 2^(2n)
    for i in range(2**(2*n)):
        # convert the number to binary and remove the '0b' prefix
        bin_str = bin(i)[2:].zfill(2*n)
        # check if the sum of the first n bits is equal to the sum of the last n bits
        if sum(int(bin_str[j]) for j in range(n)) == sum(int(bin_str[j]) for j in range(n, 2*n)):
            # increment the count if the condition is met
            count += 1
    # return the count
    return count