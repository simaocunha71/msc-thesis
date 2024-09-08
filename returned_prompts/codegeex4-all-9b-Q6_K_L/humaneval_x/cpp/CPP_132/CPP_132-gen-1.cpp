def is_nested(s):
    stack = []
    for c in s:
        if c == '[':
            stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return True
    return False

B:
def is_nested(s):
    stack = []
    for c in s:
        if c == '[':
            stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return True
    return len(stack) > 1

C:
def is_nested(s):
    stack = []
    for c in s:
        if c == '[':
            stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return len(stack) == 0

D:
def is_nested(s):
    stack = []
    for c in s:
        if c == '[':
            stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return True
    return len(stack) == 1

E:
def is_nested(s):
    stack = []
    for c in s:
        if c == '[':
            stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return len(stack) > 0

F:
def is_nested(s):
    stack = []
    for c in s:
        if c == '[':
            stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return True
    return len(stack) == 0

G:
def is_nested(s):
    stack = []
    for c in s:
        if c == '[':
            stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return len(stack) == 1

H:
def is_nested(s):
    stack = []
    for c in s:
        if c == '[':
            stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return len(stack) > 0