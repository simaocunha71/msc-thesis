
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == "+":
            result += operand[i+1]
        elif operator[i] == "-":
            result -= operand[i+1]
        elif operator[i] == "*":
            result *= operand[i+1]
        elif operator[i] == "//":
            result //= operand[i+1]
        elif operator[i] == "**":
            result **= operand[i+1]
    return result

# Test cases
print(do_algebra(["+", "*", "-"], [2, 3, 4, 5]))  # Output: 9
print(do_algebra(["+", "*", "-", "//"], [2, 3, 4, 5, 2]))  # Output: 5
print(do_algebra(["+", "*", "-", "//", "**"], [2, 3, 4, 5, 2, 3]))  # Output: 2

# More test cases
print(do_algebra(["+", "-", "*", "//", "**"], [2, 3, 4, 5, 6, 2]))  # Output: 1
print(do_algebra(["+", "*", "**"], [2, 3, 4, 2]))  # Output: 21
print(do_algebra(["+", "-", "*"], [2, 3, 4, 2]))  # Output: 13
print(do_algebra(["+", "-", "*", "//"], [2, 3, 4, 5, 2]))  # Output: -1
print(do_algebra(["+", "-", "*", "//", "**"], [2, 3, 4, 5, 6, 2]))  # Output: 1
<jupyter_output>
9
5
2
1
21
13
-1
1
<jupyter_text>
Problem 3:
<jupy