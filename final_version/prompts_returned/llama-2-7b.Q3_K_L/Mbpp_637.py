"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""
class Solution:
    def noprofit_noloss(self, price, cost):
        """
        :type price: int
        :rtype: bool
        """
        if (price - 1) < cost < (price + 1): # If the profit is not positive
            return True
        else:
            return False