    def is_nested(string):
        stack = []
        for s in string:
            if s == '[':
                stack.append(s)
            elif s == ']' and stack:
                stack.pop()
        return stack


