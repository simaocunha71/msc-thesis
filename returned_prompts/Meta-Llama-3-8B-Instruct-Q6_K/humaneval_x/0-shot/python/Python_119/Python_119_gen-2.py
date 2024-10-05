    def match_parens(lst):
        stack = []
        for char in lst[0] + lst[1]:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    return 'No'
        if stack:
            return 'No'
        return 'Yes'
    print(match_parens(['()(', ')'])) # 'Yes'
    print(match_parens([')', ')'])) # 'No'





Solution:

The function `match_parens` takes a list of two strings as input. It uses a stack to keep track of the open parentheses. 

It iterates over the characters in the concatenated string (created by joining the two input strings). If it encounters an open parenthesis, it pushes it onto the stack. If it encounters a close parenthesis, it checks if the stack is not empty. If the stack is not empty, it pops the top element (which is an open parenthesis) from the stack. If the stack is empty, it means there is no matching open parenthesis for the close parenthesis, so it returns 'No'.

After iterating over all the characters, if the stack is not empty, it means there are unmatched open parentheses, so it returns 'No'. If the stack is empty, it means all parentheses are matched, so it returns 'Yes'. 

This function works because it ensures that every open parenthesis has a corresponding close parenthesis, and vice versa, in the resulting string. If it is possible to create a good string by concatenating the two input strings, the function will return 'Yes', otherwise it will return 'No'. 

The examples provided in the problem statement demonstrate the correct functioning of this function. For example, `match_parens(['()(', ')'])` returns 'Yes' because it is possible to create a good string by concatenating these parentheses. On the other hand, `match_parens([')', ')'])` returns 'No' because it is not possible to create a good string by concatenating these parentheses.