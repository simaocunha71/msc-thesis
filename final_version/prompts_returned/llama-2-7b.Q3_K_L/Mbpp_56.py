"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""
class Solution:
    def check(self, num):
        # write your code here
        digit = '0123456789'
        reversednum = ''
        for n in range(len(digit)):
            reversednum += digit[int(len(digit) - 1)-n]
        
        result = True if int(reversednum) * 2 == num - 1 else False
        return result