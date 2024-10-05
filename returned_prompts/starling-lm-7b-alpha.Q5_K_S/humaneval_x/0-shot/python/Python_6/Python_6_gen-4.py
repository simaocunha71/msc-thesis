    def _parse(stack, cur_depth, cur_paren):
        if cur_paren == "(":
            stack.append(cur_depth)
            cur_depth += 1
        elif cur_paren == ")":
            cur_depth = stack.pop()
            cur_depth -= 1
        else:
            stack.append(cur_depth)
            cur_depth = 0

        return cur_depth, stack

    result = []
    stack = []
    for c in paren_string:
        _, stack = _parse(stack, cur_depth=0, cur_paren=c)
        if len(stack) == 0:
            result.append(0)
        else:
            result.append(stack[-1])
    return result


# print(parse_nested_parens('(()()) ((())) () ((())()())')) # [2, 3, 1, 3]
# print(parse_nested_parens('(()()()) () ((())()())')) # [2, 1, 3]
# print(parse_nested_parens('()()()')) # [0, 0, 0]




# In the above code, we use a stack to track the nesting of parentheses. We iterate over the input string and for each character, we either increment or decrement the depth of the nesting depending on whether the character is an opening or closing parenthesis. We also store the maximum depth of the nesting in the stack. If the stack is empty, it means that the depth of nesting is 0, otherwise the depth of nesting is the last element in the stack. Finally, we return a list of all depths of nesting for each group of nested parentheses.


# Here are the step by step explanations:

# We define an inner function _parse that takes three parameters: stack, cur_depth, and cur_paren. The stack parameter is a list that will store the maximum depth of nesting for each group of nested parentheses. The cur_depth parameter is the current depth of nesting and the cur_paren parameter is the current character in the input string.

# Inside the _parse function, we check if the current character is an opening parenthesis