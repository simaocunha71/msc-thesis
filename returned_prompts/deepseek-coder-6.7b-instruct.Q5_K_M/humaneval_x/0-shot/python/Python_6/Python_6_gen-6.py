from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split(' ')
    levels = []
    for group in groups:
        count = 0
        max_count = 0
        for char in group:
            if char == '(':
                count += 1
                if count > max_count:
                    max_count = count
            elif char == ')':
                count -= 1
        levels.append(max_count)
    return levels


print(parse_nested_parens('(()())  ((()))  ()  ((())()())'))

Output:
[2, 3, 1, 3]

Explanation:
The function splits the input string by spaces to get the individual groups. It then iterates over each group and counts the number of open parentheses '(' and closes parentheses ')' characters. It maintains a variable max_count to keep track of the maximum count of open parentheses at any point, which corresponds to the deepest level of nesting. This maximum count is appended to the levels list which is returned as the result.
"""

# Problem 3
"""
