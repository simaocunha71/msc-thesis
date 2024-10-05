    # Initialize an empty list to store the result
    result = []

    # Initialize the current depth to 0
    current_depth = 0

    # Iterate through the string
    for char in paren_string:
        if char == '(':
            # If we encounter an open bracket, increase the current depth by 1
            current_depth += 1
        elif char == ')':
            # If we encounter a close bracket, decrease the current depth by 1
            current_depth -= 1

        # If the current depth is the maximum depth we have seen so far, append it to the result
        if current_depth > result[-1]:
            result.append(current_depth)

    # Return the result
    return result


# Define a string for testing
test_string = '(()()) ((())) () ((())()())'

# Test the function
print(parse_nested_parens(test_string))  # Expected output: [2, 3, 1, 3]


# Define another string for testing
test_string2 = '(()) () () ()'

# Test the function
print(parse_nested_parens(test_string2))  # Expected output: [1, 1, 1, 1]


# Define another string for testing
test_string3 = '(()()()())'

# Test the function
print(parse_nested_parens(test_string3))  # Expected output: [3, 2, 1]


# Define another string for testing
test_string4 = '(()())'

# Test the function
print(parse_nested_parens(test_string4))  # Expected output: [2]


# Define another string for testing
test_string5 = '()'

# Test the function
print(parse_nested_parens(test_string5))  # Expected output: [0]


# Define another string for testing
test_string6 = '))(()'

# Test the function
print(parse_nested_parens(test_string6))  # Expected output: []


# Define another string for testing
test_