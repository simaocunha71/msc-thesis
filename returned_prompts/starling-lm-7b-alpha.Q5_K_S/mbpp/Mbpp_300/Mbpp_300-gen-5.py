"""
from itertools import product
def count_binary_seq(n):
    # Initialize result
    res = 0
    # Generate all sequences
    for seq in product([0, 1], repeat=2*n):
        # Check if condition satisfied
        if sum(seq[:n]) == sum(seq[n:]):
            res += 1
    return res
"""

# Time: O(2^n)
# Space: O(1)
class Solution(object):
    def countBinarySubstrings(self, num):
        """
        :type num: str
        :rtype: int
        """
        result = 0
        prev = None
        for i in xrange(len(num)):
            if prev is None:
                prev = int(num[i])
            elif int(num[i]) != prev:
                result += min(int(num[i]), prev)
                prev = int(num[i])
            else:
                prev = prev - 1
        return result + prev



# Time: O(n)
# Space: O(1)
class Solution2(object):
    def countBinarySubstrings(self, num):
        """
        :type num: str
        :rtype: int
        """
        result = 0
        prev, curr = 0, 1
        for i in xrange(1, len(num)):
            if int(num[i]) < int(num[i-1]):
                prev, curr = curr, 1
            else:
                curr += 1
                prev = min(prev, curr)
            result += prev
        return result



# Time: O(n)
# Space: O(1)
class Solution3(object):
    def countBinarySubstrings(self, num):
        """
        :type num: str
        :rtype: int
        """
        result = 0
        count = 1
        for i in xrange(1, len(num)):
            if int(num[i]) == int(num[i-1]):
                count += 1
            else:
                result