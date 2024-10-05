from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    temp = 0
    for char in paren_string:
        if char == '(':
            temp += 1
        elif char == ')':
            temp -= 1
        if temp == 0:
            result.append(max_level)
            max_level = 0
        max_level = max(max_level, temp)
    return result


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Expected output: [2, 3, 1, 3]
print(parse_nested_parens('()'))  # Expected output: [1]
print(parse_nested_parens('()()'))  # Expected output: [1, 1]
print(parse_nested_parens('(()())'))  # Expected output: [2]
print(parse_nested_parens('((()))'))  # Expected output: [3]
print(parse_nested_parens('((()))(()())'))  # Expected output: [3, 2]
print(parse_nested_parens('((()))(())(()())'))  # Expected output: [3, 1, 2]
print(parse_nested_parens('(()()(()())())'))  # Expected output: [2, 2, 2]
print(parse_nested_parens('((())(()())())'))  # Expected output: [3, 2, 2]
print(parse_nested_parens('((()))(())((()))'))  # Expected output: [3, 1, 3]
print(parse_nested_parens('(()((()))())'))  # Expected output: [2, 3, 1]
print(parse_nested_parens('((()))((()))'))  # Expected output: [3, 3]
print(parse_nested_parens('(()())((()))'))  # Expected output: [2, 3]
print(parse_nested_parens('((()))(())()((()))'))  # Expected output: [3, 1, 1, 3]
print(parse_nested_parens('((()))(())((()))()'))  # Expected output: [3, 1, 3, 1]
print(parse_nested_parens('(()())((()))((()))'))  # Expected output: [2, 3, 3]
print(parse_nested_parens('