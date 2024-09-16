"""
We can observe that the sum of first n bits is equal to the sum of last n bits. 
Thus, the sum of all n bits is equal to sum of all n bits. 
Therefore, the total count is 2^n.
"""
def count_binary_seq(n):
    return 2**n
