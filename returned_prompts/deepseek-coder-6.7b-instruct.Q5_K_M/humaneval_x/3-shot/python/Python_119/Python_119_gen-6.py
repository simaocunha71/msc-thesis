    from collections import deque

    open_stack = deque()
    close_stack = deque()

    for string in lst:
        for char in string:
            if char == '(':
                open_stack.append(char)
            elif char == ')' and open_stack:
                open_stack.pop()
            else:
                close_stack.append(char)

    return 'Yes' if len(open_stack) == len(close_stack) else 'No'


