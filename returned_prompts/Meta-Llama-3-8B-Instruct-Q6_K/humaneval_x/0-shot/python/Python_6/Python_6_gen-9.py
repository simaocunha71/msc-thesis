    def parse_nested_parens(paren_string: str) -> List[int]:
        result = []
        for group in paren_string.split():
            depth = 0
            max_depth = 0
            for char in group:
                if char == '(':
                    depth += 1
                elif char == ')':
                    depth -= 1
                max_depth = max(max_depth, depth)
            result.append(max_depth)
        return result

    print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
    print(parse_nested_parens('()'))  # [1]
    print(parse_nested_parens('()()'))  # [1, 1]
    print(parse_nested_parens('((()))'))  # [3]
    print(parse_nested_parens('((()))(()())'))  # [3, 2]
    print(parse_nested_parens('((()))(()())(()())'))  # [3, 2, 1]  # [3, 2, 1]
    print(parse_nested_parens('((()))(()())(()())()'))  # [3, 2, 1, 1]

    # Test case
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3], f"Expected parse_nested_parens('(()()) ((())) () ((())()())') to return [2, 3, 1, 3], but got {parse_nested_parens('(()()) ((())) () ((())()())')}"
    assert parse_nested_parens('()') == [1], f"Expected parse_nested_parens('()') to return [1], but got {parse_nested_parens('()')}"
    assert parse_nested_parens('()()') == [1, 1], f"Expected parse_nested_parens('()()') to return [1, 1], but got {parse_nested_parens('()()')}"
    assert parse_nested_parens('((()))') == [3], f"Expected parse_nested_parens('((()))') to return [3], but got {parse_nested_parens('((()))')}"
    assert parse_nested_parens('((()))(()())') == [3, 2], f"Expected parse