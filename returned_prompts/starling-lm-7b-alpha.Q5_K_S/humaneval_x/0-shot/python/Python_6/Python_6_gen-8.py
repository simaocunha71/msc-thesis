    # Parse the input string to a list of the form [(,), (,), ()]
    parsed_string = [char for char in paren_string]
    # Initialize a counter for the max depth
    max_depth = 0

    while parsed_string:
        char = parsed_string.pop(0)
        # If the char is an opening parens increment the depth
        if char == '(':
            max_depth += 1
        # If the char is a closing parens decrement the depth
        elif char == ')':
            max_depth -= 1
        # If the char is a space ignore it
        elif char == ' ':
            continue
        # If the char is none of the above add an error
        else:
            raise ValueError("Invalid character in input string")
        # After each iteration add the max depth to the result list
        max_depth_list.append(max_depth)

    return max_depth_list


# Test the function
import doctest

doctest.testmod()


# Run the tests
if __name__ == "__main__":
    parse_nested_parens('(()()) ((())) () ((())()())')
```
    
The `parse_nested_parens` function takes a string as an input, where the string has multiple groups of nested parentheses separated by spaces. The function's goal is to output the maximum depth of nesting for each group of parentheses. 

To achieve this, the function first parses the input string into a list of characters. It then initializes a counter variable `max_depth` to keep track of the maximum depth of nesting. 

The function uses a while loop to iterate through each character in the parsed string. If the character is an opening parenthesis `(`, the `max_depth` counter is incremented by 1. If the character is a closing parenthesis `)`, the `max_depth` counter is decremented by 1. If the character is a space, it is ignored. If the character is none of the above, an error is raised. 

After each iteration, the maximum depth of nesting is added to a result list called `max_depth_list`. Finally, the function returns