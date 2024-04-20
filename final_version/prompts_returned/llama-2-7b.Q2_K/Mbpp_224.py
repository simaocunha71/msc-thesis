"""
Write a python function to count the number of set bits (binary digits with value 1) in a given number.
assert count_Set_Bits(2) == 1
"""
class Solution:
    def countSetBits(self, A):
        """
        :param A: [Integer]
        :return: [Integer], [Boolean]
        if len(A) <= 64:
            return A.count('1')
        else:
            bits = [1<<i for i in range(28,32,-1)]
            return sum([bits[i] * A[len(A)-i-1:] for i in range(0, 7, -1)])
        """
        if len(A) <= 64:
            return sum(int('1' if j == k else '0' for (k,j) in zip(range(28,32), A))
                       )
        b = bytes([str(x) for x in A])
        bits = [1<<i for i in range(28, 32,-1)]
        return sum([bits[i] * b[len(b)-i-1:] for i in range(0,7,-1)])
