"""
Write a function to find the n'th star number.
assert find_star_num(3) == 37
"""
class Solution:
    def findStarNum(self, num):
        if num >= 3:
            return self._findStarSum(num-1).nextNumber
        else:
            return 0
    
    def _findStarSum(self, i):
        sum = 0
        if i == 0:
            return (1, 1)
        
        for j in range(i+1, 3650214):
            if j % 10 == 8:
                sum += 1
            else:
                continue
            
            res = self._findStarSum(j-1).nextNumber
            return (sum + res[1], sum)

# Solution:
class Solution:
    def findStarNum(self, num):
        if num >= 3:
            return self.find_star_num(len(10**num))
        else:
            return 0
    
    def find_star_num(self, n):
        list = [i for i in range(2, 45)]
        sum = []
        
        if len(list) > n:
            res = sorted((i*10**n for i in list), reverse=True)
            return res[-3]
        else:
            raise ValueError("List is too short!")
