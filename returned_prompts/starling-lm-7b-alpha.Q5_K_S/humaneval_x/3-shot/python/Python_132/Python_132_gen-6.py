    # Solution
    def is_nested(s):
        stack = []
        for c in s:
            if c == '[':
                stack.append(c)
            elif c == ']' and stack:
                stack.pop()
        return len(stack) != 0


