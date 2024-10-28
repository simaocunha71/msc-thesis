
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack

if __name__ == "__main__":
    import doctest
    doctest.testmod()



This program uses a stack to keep track of the opening brackets. When it encounters a closing bracket, it pops the last opening bracket from the stack. If the stack is empty (indicating there's no matching opening bracket for the closing bracket), it returns False. If the stack isn't empty at the end of the string (indicating there are unmatched opening brackets), it returns False. Otherwise, it returns True.

The time complexity of this program is O(n), where n is the length of the string. This is because it makes one pass over the string. The space complexity is also O(n) because in the worst case (when all brackets are opening) it might push all brackets onto the stack.

The doctest.testmod() function is used to automatically run the tests provided in the docstring.

The program is correct and efficient. It returns True for strings that are correctly bracketed and False for strings that are not.




"""


def test_correct_bracketing():
    assert correct_bracketing("(") == False
    assert correct_bracketing("()") == True
    assert correct_bracketing("(()())") == True
    assert correct_bracketing(")(()") == False
    assert correct_bracketing("") == True
    assert correct_bracketing(")(") == False
    assert correct_bracketing("(()") == False


test_correct_bracketing()
"""

"""


"""


def test_correct_bracketing():
    assert correct_bracketing("(") == False
    assert correct_bracketing("()") == True
    assert correct_bracketing("(()())") == True
    assert correct_bracketing(")(()") == False
    assert correct_bracketing("") == True
   