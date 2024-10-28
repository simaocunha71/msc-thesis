    def match_parens(lst):
        paren_stack = []
        for c in lst[0]:
            if c == '(':
                paren_stack.append(c)
            elif c == ')':
                if len(paren_stack) == 0:
                    return 'No'
                else:
                    paren_stack.pop()
        if len(paren_stack) == 0:
            for c in lst[1]:
                if c == '(':
                    paren_stack.append(c)
                elif c == ')':
                    if len(paren_stack) == 0:
                        return 'No'
                    else:
                        paren_stack.pop()
            if len(paren_stack) == 0:
                return 'Yes'
        return 'No'



























'''
To check if it's possible to concatenate the two strings,
we can just use a stack to keep track of the parentheses.
At each step, if we see an open parentheses, we push it onto the stack.
If we see a close parentheses, if the stack is empty, then it's impossible to concatenate them in
the right order, and we can return 'No'. Otherwise, we pop the stack.
At the end, if the stack is empty, then we can concatenate them in the right order, and we can return 'Yes'.
If the stack is not empty, then we can return 'No' at this point too, since there are extra open parentheses.

However, we need to consider the case where the first string has an extra close parentheses,
and the second string has an extra open parentheses.
To handle this, after checking the first string, we need to reverse the stack and push all the parentheses back into the stack.
Then, we go through the second string again, popping parentheses from the stack.
If at any point, the stack is empty, we can return 'No'.
If at the end, the stack is empty, we can return 'Yes'. Otherwise, we