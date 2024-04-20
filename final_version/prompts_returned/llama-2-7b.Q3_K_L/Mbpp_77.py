"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""
class Solution:
    def isDivisibleBy11(self, num):
        # base case first
        if num % 11 <= 0:
            return True if num%11==0 else False
        
        # recursion here
        result = self.is_Diff(num//11) and True or False

        return result

def is_Diff (num):
    """
    function to find the diffence of any two numbers
    :param num:
    :return:
    1) if num == 0 then return false else return true
    2) if num not zero and divisible by 3 then return True, else False
    """
    # base case first
    if num==0:
        return False

    # condition to get the diffence of any two numbers
    if num % 10 == 9 or num%3 != 0:
        return False
    return True

# Test Cases
assert Solution().isDivisibleBy11(1248)==True
