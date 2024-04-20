"""
Write a function to remove leading zeroes from an ip address.
assert removezero_ip("216.08.094.196")==('216.8.94.196')
"""
class Solution:
    def removeZero(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ''
        for idx in range(len(s) - 1):
            if s[idx] != '0':
                break
            else:
                res += s[idx]
        return res
