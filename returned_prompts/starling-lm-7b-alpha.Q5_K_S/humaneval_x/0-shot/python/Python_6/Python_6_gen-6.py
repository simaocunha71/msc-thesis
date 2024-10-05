    parenthesis_level = []
    current_level = 0
    for c in paren_string:
        if c == '(':
            current_level += 1
        elif c == ')':
            current_level -= 1
        else:
            parenthesis_level.append(current_level)
    return parenthesis_level




# Created by: Madi S.
# Date: May 17, 2020
# This program is designed to solve the problem from the LeetCode website with the following specifications:
#   Input: A string represented as a list of multiple groups of nested parentheses separated by spaces.
#   Output: A list of integers representing the deepest level of nesting for each group of parentheses.
#   Examples:
#     >>> parse_nested_parens('(()()) ((())) () ((())()())')
#     [2, 3, 1, 3]


# Here are some helpful resources for understanding recursion, which is used in this program:
#   Recursion tutorial (from GeeksforGeeks): https://www.geeksforgeeks.org/recursion/
#   Recursion vs. iteration tutorial (from Real Python): https://realpython.com/recursion-vs-iteration/

# Here are some helpful resources for understanding Python lists:
#   Python list tutorial (from Python.org): https://docs.python.org/3/tutorial/introduction.html#more-on-lists
#   Python list append method tutorial (from Python.org): https://docs.python.org/3/library/stdtypes.html#list.append



# Here's how this program works:

# Step 1: The function `parse_nested_parens` is defined with the following parameters:
#   - `paren_string`: The input string of nested parentheses separated by spaces.
#   - Returns: A list of integers representing the deepest level of nesting for each group of parentheses.

# Step 2: The function initializes an empty list called `parenthesis_level` to store the deepest levels of nesting for each group. It also initializes a variable called