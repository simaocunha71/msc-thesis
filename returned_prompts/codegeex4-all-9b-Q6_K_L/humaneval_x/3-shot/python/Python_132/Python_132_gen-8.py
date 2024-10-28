    def is_valid(s):
        stack = []
        for c in s:
            if c == '[':
                stack.append(c)
            elif c == ']':
                if len(stack) == 0:
                    return False
                stack.pop()
        return len(stack) == 0

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if is_valid(string[i:j]):
                return True
    return False

