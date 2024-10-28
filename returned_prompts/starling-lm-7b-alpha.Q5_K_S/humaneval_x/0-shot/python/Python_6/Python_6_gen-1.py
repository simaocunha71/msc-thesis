    paren_levels = []
    current_level = 0
    for char in paren_string:
        if char == '(':
            current_level += 1
        elif char == ')':
            current_level -= 1
        else:
            paren_levels.append(current_level)

    return paren_levels


# Test cases
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Expected: [2, 3, 1, 3]
print(parse_nested_parens('(((()))())))'))  # Expected: [4, 3, 2]
print(parse_nested_parens('()'))  # Expected: [0]
print(parse_nested_parens('(()()()()))'))  # Expected: [2, 3, 2, 1]


# Here's how the function works:

# Initialize an empty list to store the levels of nesting.
# Initialize a variable called current_level to zero. This variable will keep track of the current level of nesting
# while iterating through the string.

# Iterate through the string character by character. For each character:
# If the character is an opening parenthesis '(', increment the current_level by 1.
# If the character is a closing parenthesis ')', decrement the current_level by 1.
# If the character is neither an opening nor a closing parenthesis, append the current_level to the paren_levels list.

# After iterating through the entire string, the function should return the paren_levels list.


# Time complexity: O(n), where n is the length of the input string.

# Space complexity: O(n), where n is the length of the input string. This is because we're storing the maximum
# level of nesting for each group of nested parentheses in the paren_levels list.






# The time and space complexity of this function is O(n). This is because we're iterating through the entire string and
# storing the maximum nesting level for each group of nested parentheses in a list.


