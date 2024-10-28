    def helper(lst):
        if len(lst) == 0:
            return True
        if lst[0] == '(':
            return helper(lst[1:])
        if len(lst) >= 2 and lst[0] == ')' and lst[1] == '(':
            return helper(lst[2:])
        return False

    return 'Yes' if helper(lst) else 'No'  # Pythonic way
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # if helper(lst):
    #     return 'Yes'
    # else:
    #     return 'No'  # Without using Python's conditional expression
    # if helper(lst):
    #     return 'Yes'
    # else: return 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without using Python's conditional expression
    # return 'Yes' if helper(lst) else 'No'  # Without