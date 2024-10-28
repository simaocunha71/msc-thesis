    def separate_paren_groups(paren_string: str) -> List[str]:
        groups = []
        current_group = ''
        for char in paren_string:
            if char == '(':
                current_group += char
            elif char == ')':
                current_group += char
                groups.append(current_group)
                current_group = ''
            else:
                current_group += char
        return groups



