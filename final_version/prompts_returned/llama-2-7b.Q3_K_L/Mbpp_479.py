"""
Write a python function to find the first digit of a given number.
assert first_Digit(123) == 1
"""
class Solution:
    def firstDigit(self, n):
        if not isinstance(n,(int)): #if type(n)==int and n>=0 then it wont be integer overflow
            return None
        else:
            digit=0
            for i in range(1,len(str(n))-1):
                digit =digit + (n/pow(10,i))%10
            return digit

s = Solution() # creating an object of the class solution
print( s.firstDigit(987654321) )