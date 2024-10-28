    def parse_nested_parens_helper(paren_string: str) -> int:
        max_depth = 0
        depth = 0
        for char in paren_string:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    return [parse_nested_parens_helper(part) for part in paren_string.split()]









# Python3 program to find maximum depth of 
# nested parentheses in an expression 

# Function to find maximum depth of 
# nested parentheses in an expression 
def max_depth_nested_parentheses(str): 
    max_depth = 0
    depth = 0
    for i in range(len(str)): 
        if (str[i] == '('): 
            depth += 1
            max_depth = max(max_depth, depth) 
        elif (str[i] == ')'): 
            depth -= 1
    return max_depth

# Driver program 
if __name__ == "__main__": 
    str = "(((()())(())()))"
    print(max_depth_nested_parentheses(str))





































































































































































































