
def check_expression(expr: str) -> bool:
    stack = []
    open_set = set(["(", "{", "["])
    close_set = set([")", "}", "]"])
    for c in expr:
        if c in open_set:
            stack.append(c)
        elif c in close_set:
            if len(stack) == 0 or close_set.index(c) != open_set.index(stack.pop()):
                return False
    return len(stack) == 0


