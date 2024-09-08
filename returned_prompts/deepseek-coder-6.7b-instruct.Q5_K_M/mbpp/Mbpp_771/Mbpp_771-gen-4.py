
def check_expression(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}

    for char in expression:
        if char in brackets.keys():
            stack.append(char)
        elif len(stack) == 0 or brackets[stack.pop()] != char:
            return False
    return len(stack) == 0

print(check_expression("{()}[{}]"))  # True

# Time complexity: O(n), n is the length of the given expression
# Space complexity: O(n) in the worst case scenario when all the brackets are opening brackets, we will end up pushing all of them onto the stack.

# Explanation:
# We are using a stack data structure to solve this problem.
# We iterate through each character in the given expression.
# If the character is an opening bracket, we push it onto the stack.
# If the character is a closing bracket, we pop the last element from the stack and compare it with the current closing bracket.
# If they match, we continue, if not, we return False.
# After going through all the characters in the expression, if there are still elements in the stack, it means that there are unmatched opening brackets, so we return False.
# If there are no unmatched brackets, we return True.
<jupyter_output>
True
<jupyter_text>
Problem 2:
<jupyter_code>
