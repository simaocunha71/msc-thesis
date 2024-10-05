
def do_algebra(operator, operand):
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += ' ' + operator[i] + ' ' + str(operand[i+1])
    return eval(expression)

# Testing
print(do_algebra(["+", "-"], [5, 4, 3]))  # Should return 6
print(do_algebra(["*", "/"], [6, 2, 3]))  # Should return 3
print(do_algebra(["**"], [2, 3]))  # Should return 8
<jupyter_output>
6
3
8
<jupyter_text>
Problem 3Given a string, count the number of words in the string. Words in the string are separated by spaces. You can assume that the string has no punctuation marks and only contains spaces and alphanumeric characters.
<jupyter_code>
