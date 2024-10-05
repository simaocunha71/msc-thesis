    def is_balanced(string):
        balanced = 0
        for char in string:
            if char == '(':
                balanced += 1
            elif char == ')':
                balanced -= 1
            if balanced < 0:
                return False
        return balanced == 0

    return 'Yes' if is_balanced(lst[0] + lst[1]) else 'No'
