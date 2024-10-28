    def parse_nested_parens_helper(paren_string: str) -> int:
        result = 0
        for c in paren_string:
            if c == '(':
                result += 1
            if c == ')':
                result -= 1
        return result

    return [parse_nested_parens_helper(group) for group in paren_string.split()]


