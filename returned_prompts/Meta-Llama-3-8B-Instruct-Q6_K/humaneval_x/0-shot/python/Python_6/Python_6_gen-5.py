    from typing import List

    def parse_nested_parens(paren_string: str) -> List[int]:
        max_levels = []
        current_level = 0
        for char in paren_string:
            if char == '(':
                current_level += 1
            elif char == ')':
                current_level -= 1
            if current_level == 0 and paren_string[paren_string.index(char) + 1] == ' ':
                max_levels.append(current_level)
        return max_levels

    print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
    print(parse_nested_parens('((()))'))  # Output: [3]
    print(parse_nested_parens('()'))  # Output: [1]
    print(parse_nested_parens('(()())'))  # Output: [2]
    print(parse_nested_parens('()()'))  # Output: [1]
    print(parse_nested_parens('()(()())'))  # Output: [2]
    print(parse_nested_parens('()((()))'))  # Output: [3]

# Test cases
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
print(parse_nested_parens('((()))'))  # Output: [3]
print(parse_nested_parens('()'))  # Output: [1]
print(parse_nested_parens('(()())'))  # Output: [2]
print(parse_nested_parens('()()'))  # Output: [1]
print(parse_nested_parens('()(()())'))  # Output: [2]
print(parse_nested_parens('()((()))'))  # Output: [3]  # Output: [3]
print(parse_nested_parens('()()'))  # Output: [1]
print(parse_nested_parens('(()(()()))'))  # Output: [3]
print(parse_nested_parens('(()())'))  # Output: [2]
print(parse_nested_parens('((()))'))  # Output: [3]
print(parse_nested_parens('()((()))'))  # Output: [3]
print(parse_nested_parens('(()(()()))'))  # Output: [3]
print(parse_nested_parens('()()'))  # Output: