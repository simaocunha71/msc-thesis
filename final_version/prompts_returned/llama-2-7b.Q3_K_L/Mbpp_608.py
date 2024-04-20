"""
Write a python function to find nth bell number.
assert bell_Number(2) == 2
"""
class Solution:
    def bell_number(self, n):
        res = [1]
        
        for i in range(n-1):
            res.append(res[i]*3+res[-1])
            
        return sum(res)