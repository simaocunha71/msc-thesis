    levels := 0
    res := []int{}
    for _, c := range paren_string {
        if c == '(' {
            levels++
        } else if c == ')' {
            levels--
        }
        if levels > len(res) {
            res = append(res, levels)
        }
    }
    return res
}

# Python

# Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
# For each of the group, output the deepest level of nesting of parentheses.
# E.g. (()()) has maximum two levels of nesting while ((())) has three.
# 
# >>> ParseNestedParens('(()()) ((())) () ((())()())')
# [2, 3, 1, 3]
def ParseNestedParens(paren_string):
    levels = 0
    res = []
    for c in paren_string:
        if c == '(':
            levels += 1
        elif c == ')':
            levels -= 1
        if levels > len(res):
            res.append(levels)
    return res

# Python

# The function below should return an array of maximum depth of parentheses in a string that contains multiple groups of nested parentheses.
# Each group of parentheses is separated by a space.
# For example, (()()) has a maximum of two levels of nesting, while ((())) has three.
# >>> ParseNestedParens('(()()) ((())) () ((())()())')
# [2, 3, 1, 3]
def ParseNestedParens(paren_string):
    levels = 0
    res = []
    for c in paren_string:
        if c == '(':
            levels += 1
        elif c == ')':
            levels -= 1
        if levels > len(res):
            res.append(levels)
    return res

# Python

# The function below should return an array of maximum depth of parentheses in a string that contains multiple groups of nested parentheses.
# Each group of parentheses is separated by a space.
