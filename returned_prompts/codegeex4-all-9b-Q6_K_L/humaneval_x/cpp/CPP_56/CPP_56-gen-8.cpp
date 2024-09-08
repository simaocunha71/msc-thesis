def correct_bracketing(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '<':
            stack.append(bracket)
        elif bracket == '>':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

B:
def correct_bracketing(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '<':
            stack.append(bracket)
        elif bracket == '>':
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return len(stack) == 0

C:
def correct_bracketing(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '<':
            stack.append(bracket)
        elif bracket == '>':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

D:
def correct_bracketing(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '<':
            stack.append(bracket)
        elif bracket == '>':
            if len(stack) > 0:
                stack.pop()
    return len(stack) == 0

E:
def correct_bracketing(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '<':
            stack.append(bracket)
        elif bracket == '>':
            stack.pop()
    return len(stack) == 0
