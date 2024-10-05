
    def match_parens(lst):
        s = lst[0] + lst[1]
        stack = []
        for p in s:
            if p == '(':
                stack.append(p)
            elif p == ')' and stack:
                stack.pop()
            else:
                return 'No'
        return 'Yes' if not stack else 'No'

    print(match_parens(['()(', ')']))  # 'Yes'
    print(match_parens([')', ')']))  # 'No'

In this solution, we first concatenate the two strings. Then, we initialize an empty stack to keep track of open parentheses. For each character in the string, if it is an open parentheses, we push it to the stack. If it is a close parentheses, we check if the stack is not empty. If the stack is not empty, we pop the top element from the stack. If the stack is empty, we return 'No' as there is a closing parenthesis without a corresponding opening parenthesis. After we have processed all characters in the string, if the stack is empty, we return 'Yes' as all parentheses are balanced. If the stack is not empty, we return 'No' as there are unbalanced parentheses.


'''

'''



'''

'''

'''

'''

'''



'''



'''










































































































































































