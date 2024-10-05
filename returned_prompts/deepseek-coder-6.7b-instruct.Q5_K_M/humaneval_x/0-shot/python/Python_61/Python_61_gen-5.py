
    stack = []

    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                return False
            stack.pop()

    return not stack


if __name__ == '__main__':
    import doctest
    doctest.testmod()


The function uses a stack to store the opening brackets. When it encounters a closing bracket, it pops the last opening bracket from the stack. If the stack is empty (indicating that there is no corresponding opening bracket for the closing bracket), it returns False. If it finishes scanning the string without the stack being empty, it also returns False (indicating that there are unmatched opening brackets). If it finishes scanning the string with the stack being empty, it returns True.
"""


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


if __name__ == "__main__":
    import doctest

    doctest.testmod()

#test_correct_bracketing.py
from correct_bracketing import correct_bracketing


def test_correct_bracketing():
    assert correct_bracketing("(") == False
    assert correct_bracketing("()") == True
    assert correct_bracketing("(()())") == True
    assert correct_bracketing(")(()") == False
    assert correct_bracketing("())(())(((") == False
    assert correct_bracketing("((()))") == True
    assert correct_bracketing("") == True
    assert correct_bracketing(")))))(((") == False
    assert correct_bracketing("((())())") == True
    assert correct_bracketing("((())()()())") == True
    assert correct_bracketing("((())()()())()") == True
    assert