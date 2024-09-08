def check_expression(expression: str) -> bool:
    open_brackets = set(["(", "[", "{"])
    close_brackets = set([")", "]", "}"])
    stack = []
    
    for char in expression:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack:
                return False
            if open_brackets.index(stack.pop()) != close_brackets.index(char):
                return False
    
    return not stack