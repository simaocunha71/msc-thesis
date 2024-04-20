"""
Write a function to check if the given expression is balanced or not. 
assert check_expression("{()}[{}]") == True
"""
import re
def check_expression(exp):
    r=re.findall(r'([a-z]+)|\([^)]+\)/?$', exp)#Regex to find all the valid tokens in an expression
    if len(r)>1:
        res='N'
        
    else: 
        res='Y'
    return res

print('N')
check_expression("{()}[{}]")