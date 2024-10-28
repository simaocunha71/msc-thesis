from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    for group in paren_string.split():
        level = 0
        max_level = 0
        for char in group:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1
        result.append(max_level)
    return result
# You can test this function with the following code:
if __name__ == "__main__":
    print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Expected output: [2, 3, 1, 3]
# The function works by iterating over each group of parentheses in the input string, and for each group, it counts the maximum level of nesting. It uses a stack (implemented as a variable 'level') to keep track of the current level of nesting, and another variable 'max_level' to keep track of the maximum level seen so far. When it encounters a '(', it increments the level, and when it encounters a ')', it decrements the level. The maximum level seen so far is updated whenever it sees a '(' at a higher level than the current maximum. The maximum level for each group is appended to the result list. Finally, the function returns the result list.