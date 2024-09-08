def parse_nested_parens(paren_string):
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens("(()()) ((())) () ((())()())")
    {2, 3, 1, 3}
    """
    #split the paren_string into groups
    groups = paren_string.split(' ')

    #initialize a vector to hold the results
    result = []

    #loop through each group
    for group in groups:
        #initialize a variable to hold the current level of nesting
        current_level = 0
        #initialize a variable to hold the maximum level of nesting
        max_level = 0

        #loop through each character in the group
        for char in group:
            #if the character is an opening parenthesis, increase the level of nesting
            if char == '(':
                current_level += 1
            #if the character is a closing parenthesis, decrease the level of nesting
            elif char == ')':
                current_level -= 1
            #if the current level of nesting is greater than the maximum level, update the maximum level
            if current_level > max_level:
                max_level = current_level

        #add the maximum level to the result vector
        result.append(max_level)

    #return the result vector
    return result

print(parse_nested_parens("(()()) ((())) () ((())()())"))