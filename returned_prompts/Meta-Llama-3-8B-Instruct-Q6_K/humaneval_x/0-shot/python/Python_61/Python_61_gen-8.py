def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if not stack:
                return False
            stack.pop()
    return not stack
# The time complexity is O(n), where n is the length of the input string.
# The space complexity is O(n), as in the worst case, all the brackets are opening brackets and we end up pushing all of them to the stack.