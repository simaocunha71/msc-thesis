    def helper(lst):
        if lst[0] == ')' or lst[-1] == '(':
            return False
        return helper(lst[:len(lst)//2]) and helper(lst[len(lst)//2:])
    return 'Yes' if helper(lst) else 'No'


