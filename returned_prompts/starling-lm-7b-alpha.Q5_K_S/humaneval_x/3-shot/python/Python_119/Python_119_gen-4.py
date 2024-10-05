    def helper(stack, idx):
        if idx == len(stack):
            return True
        if stack[idx] == '(':
            return helper(stack, idx + 1)
        else:
            if len(stack) == 0:
                return False
            else:
                return helper(stack[:idx] + stack[idx + 1 :], idx + 1)

    return helper(lst[0], 0) or helper(lst[1], 0)


