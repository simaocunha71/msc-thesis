"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""
class Solution:
    def getMaxSum(self, num):
        res = 0
        
        def helper(num, sumLeft, sumRight):
            if not (2*int(num/4)+1 <= len(str(num))-3 and 2*(int(len(str(num))-1)/3+1) <= len(str(num)):
                return res
            
            sumLeft = helper(int(num/4), sumLeft, sumRight - sumLeft)
            sumRight = helper(int(num/5), sumLeft, sumRight - sumLeft)
            
            ans = max((sumLeft + sumRight), (2*int(num/4)+1)*(2*(int(len(str(num))-1)/3+1)))
            return res if ans > res else ans
        
        helper(int(num), int(int(num) / 5), int(int(num) / 4))