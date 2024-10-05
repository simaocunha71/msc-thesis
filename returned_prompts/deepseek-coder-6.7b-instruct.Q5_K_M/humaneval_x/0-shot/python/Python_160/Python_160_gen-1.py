
    def do_algebra(operator, operand):
        result = operand[0]
        for i in range(len(operator)):
            if operator[i] == '+':
                result += operand[i+1]
            elif operator[i] == '-':
                result -= operand[i+1]
            elif operator[i] == '*':
                result *= operand[i+1]
            elif operator[i] == '//':
                result //= operand[i+1]
            elif operator[i] == '**':
                result **= operand[i+1]
        return result

# Test Cases:

assert do_algebra(["+", "-"], [10, 20, 30]) == 0
assert do_algebra(["+", "*"], [1, 2, 3, 4]) == 11
assert do_algebra(["*", "//"], [1, 2, 3, 4]) == 2
assert do_algebra(["+", "**"], [1, 2, 3, 4]) == 1025
assert do_algebra(["+", "-", "*"], [5, 5, 5, 5]) == 25
assert do_algebra(["+", "-", "*", "//"], [10, 20, 30, 40, 50]) == 50
assert do_algebra(["+", "-", "*", "//", "**"], [1, 2, 3, 4, 5, 6]) == 120

# The above test cases are valid because they test all possible operators and the function should be able to handle them all.
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2: Find the Second Largest Number in a List
<jupyter_code>
