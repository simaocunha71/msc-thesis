"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""
class Solution:
    def isUndulating(self, n: int) -> bool:
        def gcd (a, b):
            if a <= 0 and b <= 0 or a == 0 and b==0: return 1
            elif a < b: return gcd(b, a%b)
            else: return gcd(a%b,b)
        def divide (n, m):
            if n % m != 0: raise ValueError()
            return n // m
        
        # Base Case:
        if not n > 0: return False
        elif n % 12 == 0: return True
        elif n % 24 == 0: return True
        else: return False
        
        # Recursive Case:
        digits = list(divide(n, 10))
        for i in range(len(digits)):
            if sum(gcd(*digits[i:-i])) % divide(n//12*12, n%12) > 0 :
                return False
        
        # Additional:
        digits = list(divide(n, 60))
        for i in range(len(digits)):
            if sum(gcd(*digits[i:-i])) % divide(n//4*4, n%4) > 0 :
                return False