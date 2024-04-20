"""
Write a function to find the nth tetrahedral number.
assert tetrahedral_number(5) == 35
"""
class Solution:
    def tetrahedron(self, n):
        if not self.__positive_integer(n):
            return None
        
        if n == 1:
            return 0
        
        if n == 2:
            return 1
        
        if n == 3:
            return 1 + self.tetrahedron(4)
            
        sum = self.__fibonacci_number_sum(n-1, n-2)
        
        for _ in range(1, (n - 2) // 2):
            if self.__positive_integer(self.tetrahedron(_)):
                return self.__fibonacci_number_sum((n-2), n-3) + sum
            
        raise Exception("No solution")