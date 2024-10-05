def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    res = []
    last_index = 0
    for i, ch in enumerate(paren_string):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            start = stack.pop()
            if not stack:
                res.append(paren_string[start:i+1])
    return res

print(separate_paren_groups('(  )  (( ))  (( )( ))'))

"""
This solution works by using a stack to keep track of the indices of open parentheses. When a closing parenthesis is encountered, 
it pops the last index from the stack and uses it to form a substring that starts from the last index and ends at the current index. 
This substring is added to the result list. The stack is empty when a closing parenthesis is encountered, which means a separate group 
of parentheses has been found. 

The time complexity of this solution is O(n), where n is the length of the string. 
The space complexity is also O(n), as in the worst case scenario, all the parentheses could be unbalanced and be pushed into the stack.
"""

# 