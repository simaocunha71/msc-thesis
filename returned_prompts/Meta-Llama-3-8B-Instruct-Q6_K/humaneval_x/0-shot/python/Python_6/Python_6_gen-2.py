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

    if __name__ == "__main__":
        print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
        print(parse_nested_parens('((()))'))  # [3]
        print(parse_nested_parens('()'))  # [1]
        print(parse_nested_parens('()()'))  # [1, 1]
        print(parse_nested_parens('((())) ()'))  # [3, 1]    
        print(parse_nested_parens('() (()())'))  # [1, 2]
        print(parse_nested_parens('() (())'))  # [1, 1]
        print(parse_nested_parens('((())) ((()))'))  # [3, 3]
        print(parse_nested_parens('((())) ((())) ()'))  # [3, 3, 1]
        print(parse_nested_parens('() (()()) ((()))'))  # [1, 2, 3]
        print(parse_nested_parens('() (()()) ((())) ()'))  # [1, 2, 3, 1]    
        print(parse_nested_parens(''))  # []
        print(parse_nested_parens('('))  # [1]
        print(parse_nested_parens(')'))  # [0]
        print(parse_nested_parens('()('))  # [1, 0]
        print(parse_nested_parens('(()('))  # [2, 0]
        print(parse_nested_parens('((('))  # [3]
        print(parse_nested_parens('())'))  # [1]
        print(parse_nested_parens('(()')  # [2]
        print(parse_nested_parens('((('))  # [3]
        print(parse_nested_parens(')))'))  # [2]
        print(parse_nested_parens('((())) ((()))