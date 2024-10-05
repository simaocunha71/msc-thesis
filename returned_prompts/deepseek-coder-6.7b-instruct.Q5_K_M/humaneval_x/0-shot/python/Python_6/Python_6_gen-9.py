def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    groups = paren_string.split(' ')
    for group in groups:
        count = 0
        max_count = 0
        for char in group:
            if char == '(':
                count += 1
                max_count = max(max_count, count)
            elif char == ')':
                count -= 1
        result.append(max_count)
    return result


print(parse_nested_parens('(()()) ((())) () ((())()())'))



