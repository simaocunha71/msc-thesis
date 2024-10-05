    from typing import List

    def parse_nested_parens(paren_string: str) -> List[int]:
        result = []
        for group in paren_string.split():
            nesting = 0
            max_nesting = 0
            for char in group:
                if char == '(':
                    nesting += 1
                elif char == ')':
                    nesting -= 1
                max_nesting = max(max_nesting, nesting)
            result.append(max_nesting)
        return result

    print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
    # Output is a list of maximum nesting level for each group
    # For each group, output the deepest level of nesting of parentheses.
    # E.g. (()()) has maximum two levels of nesting while ((())) has three.
    # It calculates the maximum nesting level for each group. A group is a set of parentheses enclosed in spaces.
    # The function splits the input string into groups by splitting at each space.
    # For each group, it counts the nesting level by incrementing a counter whenever it encounters an open parenthesis and decrementing it whenever it encounters a close parenthesis.
    # The maximum nesting level is the maximum value of the nesting level counter during the process.
    # The function returns a list of maximum nesting levels for all groups.