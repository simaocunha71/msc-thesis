    def parse_nested_parens(paren_string: str) -> List[int]:
        stack = []
        max_level = 0
        for i in paren_string:
            if i == '(':
                stack.append(i)
            elif i == ')':
                stack.pop()
            else:
                continue
            max_level = max(max_level, len(stack))
        return [max_level]


    # Using recursion:
    def parse_nested_parens(paren_string: str) -> List[int]:
        def max_level(paren_string: str, level: int = 0):
            if not paren_string:
                return level
            if paren_string[0] == '(':
                return max_level(paren_string[1:], level + 1)
            elif paren_string[0] == ')':
                return max_level(paren_string[1:], level - 1)
            else:
                return max_level(paren_string[1:], level)

        return [max_level(i) for i in paren_string.split()]

    return parse_nested_parens(paren_string)

























































































































































































































