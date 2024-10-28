def count_binary_seq(n):
    # Total number of binary sequences of length 2n is 2^2n.
    total_seq = 2 ** (2 * n)
    
    # For the sum of first n bits to be equal to sum of last n bits, we have 2^n choices for each bit.
    # So, number of such sequences is (2^n)^2.
    equal_sum_seq = (2 ** n) ** 2
    
    # Total number of sequences where sum of first n bits is not equal to sum of last n bits is total_seq - equal_sum_seq.
    not_equal_sum_seq = total_seq - equal_sum_seq
    
    return equal_sum_seq, not_equal_sum_seq