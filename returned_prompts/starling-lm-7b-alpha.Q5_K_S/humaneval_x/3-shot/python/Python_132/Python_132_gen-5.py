    def is_nested(string):
        stack = []

        for i in string:
            if i == '[':
                stack.append(i)
            elif i == ']':
                if len(stack) == 0:
                    return True
                else:
                    stack.pop()
        return False


