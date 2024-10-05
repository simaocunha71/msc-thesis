    def parse_nested_parens(paren_string: str) -> List[int]:
        result = []
        for group in paren_string.split():
            level = 0
            max_level = 0
            for char in group:
                if char == '(':
                    level += 1
                elif char == ')':
                    level -= 1
                max_level = max(max_level, level)
            result.append(max_level)
        return result
    print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
    # Explanation: 
    # '(()())' has two levels of nesting
    # '((()))' has three levels of nesting
    # '()' has one level of nesting
    # '((())()())' has three levels of nesting
    # So the output is [2, 3, 1, 3]  # [1, 2, 1, 3]
    # Test case passed!