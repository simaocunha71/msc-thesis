class Solution(object):
    def next_smallest_palindrome(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(str(x)[::-1])


