```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Split the input string into individual groups
    groups = paren_string.split()

    # Initialize the list to store the maximum nesting levels
    max_nesting_levels = []

    # Iterate over each group
    for group in groups:
        # Initialize the current level and maximum level
        current_level = 0
        max_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the level
            if char == '(':
                current_level += 1
                # Update the maximum level if necessary
                max_level = max(max_level, current_level)
            # If the character is a closing parenthesis, decrease the level
            elif char == ')':
                current_level -= 1

        # Append the maximum nesting level for the current group to the list
        max_nesting_levels.append(max_level)

    # Return the list of maximum nesting levels
    return max_nesting_levels
```

This solution splits the input string into individual groups and then iterates over each group. For each group, it keeps track of the current level of nesting and the maximum level observed. It then updates the maximum level whenever an opening parenthesis is encountered and decreases the level when a closing parenthesis is encountered. Finally, it appends the maximum nesting level for each group to a list and returns the list.