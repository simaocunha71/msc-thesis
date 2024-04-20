"""
Write a function to check if the given expression is balanced or not. 
assert check_expression("{()}[{}]") == True
"""
class Solution(object):
    def checkBalance(self, expression):
        stack = []
        stk_len = len(stack)
        
        for i in range(1,stk_len+1): # from 1 to stk_len + 1. 
            if not self.checkBalancedExpression(i,expression):
                return False
            
        return True