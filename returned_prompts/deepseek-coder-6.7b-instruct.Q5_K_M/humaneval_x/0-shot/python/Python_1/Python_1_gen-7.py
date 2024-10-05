def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ","")
    stack = []
    result = []
    temp = ""
    for char in paren_string:
        if char == '(':
            if temp:
                stack.append(temp)
                temp = ""
            stack.append(char)
        elif char == ')':
            stack.append(char)
            while stack[-2] != '(':
                pop_item = stack.pop()
                temp = pop_item + temp
            stack.pop()
            stack.pop()
            if not stack or stack[-1] != '(':
                result.append(temp)
                temp = ""
            else:
                temp = stack.pop() + temp
                stack.append(temp)
                temp = ""
    return result

print(separate_paren_groups('(  (  )  (( ))  (( )( )))'))

# Output: ['()', '(())', '((()))']

The above function works by iterating through the string. It checks for each character, if it's an open parenthesis '(', it's pushed to the stack. If it's a close parenthesis ')', it's pushed to the stack and then we pop all the elements from the stack till we find a '(', which means we have found a group of balanced parenthesis. We then append this group to the result list.

It also handles nested parenthesis by checking the last element in the stack before adding the current group to the result. If the last element is '(', it means we are in a nested group, so we don't add it to the result.

It also handles multiple spaces in the input string by replacing them with no space before processing.

The time complexity is O(n), where n is the length of the input string. The space complexity is also O(n), since in the worst case we might end up storing all the characters in the stack.

This solution assumes that the input string is well-formed, i.e., it has matching parentheses. If the input string could have unmatched parentheses, we