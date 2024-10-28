"""
We can solve it by generating all possible binary sequences and then counting them.
"""

def count_binary_seq(n):
    count = 0
    for i in range(2**(2*n)):
        binary_seq = bin(i)[2:]
        if binary_seq[:n] == binary_seq[n:]:
            count += 1
    return count

"""
The number of possible binary sequences is 2**(2*n), and the number of sequences with the same sum for first and last n bits is 2**n.
"""
