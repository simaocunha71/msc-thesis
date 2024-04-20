"""
Write a function to find the nth hexagonal number.
assert hexagonal_num(10) == 190
"""
class Solution:
    def hexagonalNumber(self, n):
        if not isinstance(n,(int)):raise TypeError('n must be an integer')
        if not isinstance((n+2), (int)):raise TypeError('n+2 must be an integer')
        if n<1 or n==0:return 1
        elif n<4:return 1
        else:
            d = [[None,2,1],[2,3,1]]
            
            for i in range(n-4):
                print('d[i][0] == ', d[i][0])
                if d[i+1][0]:
                    a=d[i][0]+1
                    b = d[i][1]+2
                    
                else:
                    a=d[i][1]+3
                    b=d[i+1][1]
                d.append([a,b])
        return  self.sum(d)
        