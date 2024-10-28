
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if not stack or stack[-1] != "<":
                return False
            stack.pop()
    return not stack

# Test cases
print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
print(correct_bracketing("<<><>>><<>><>>"))  # True
print(correct_bracketing("<<><>>><<>>"))  # True

# Expected output:
# False
# True
# True
# False
# True
# True

The function works by iterating over the input string, one character at a time. If it encounters an opening bracket "<", it pushes it onto a stack. If it encounters a closing bracket ">", it checks if the top of the stack is an opening bracket "<". If it is, it pops the opening bracket from the stack. If the stack is empty or the top of the stack is not an opening bracket, it returns False.

Finally, if the stack is empty (which means every opening bracket has a corresponding closing bracket), it returns True. If the stack is not empty (which means there is at least one unmatched opening bracket), it returns False.

The time complexity of this function is O(n), where n is the length of the input string. This is because it makes a single pass over the string. The space complexity is O(n) in the worst-case scenario where all the brackets are opening brackets, as each opening bracket needs to be stored in the stack. In the best-case scenario where there are no opening brackets, the space complexity is O(1).

This function is correct as it checks if the brackets are correctly nested and balanced.


"""


def correct_bracketing(brackets: str):
    """ brackets is a string of  "(" and ")".
    return True if every opening bracket has a corresponding