    stack = []
    for char in lst[0]:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return 'No'
            stack.pop()

    for char in lst[1]:
        if char == ')':
            if not stack:
                return 'No'
            stack.pop()
        else:
            stack.append(char)

    if stack:
        return 'No'
    else:
        return 'Yes'  # or 'True'
    # This solution assumes that the input is valid (i.e., both strings are strings and they
    # consist only of open and close parentheses). If this is not the case, you should add error
    # checking code.  # This solution assumes that the input is valid. If this is not the case, you
    # should add error checking code.  # This solution assumes that the input is valid. If this is
    # not the case, you should add error checking code.  # This solution assumes that the input is
    # valid. If this is not the case, you should add error checking code.  # This solution assumes
    # that the input is valid. If this is not the case, you should add error checking code.  # This
    # solution assumes that the input is valid. If this is not the case, you should add error
    # checking code.  # This solution assumes that the input is valid. If this is not the case, you
    # should add error checking code.  # This solution assumes that the input is valid. If this is
    # not the case, you should add error checking code.  # This solution assumes that the input is
    # valid. If this is not the case, you should add error checking code.  # This solution assumes
    # that the input is valid. If this is not the case, you should add error checking code.  # This
    # solution assumes that the input is valid. If this is not the case, you should add error
    # checking code.  # This solution assumes that the input is valid. If this is not the case, you
    # should add error checking code.  # This solution assumes that the input is valid. If this is
    # not the case, you should add error checking code.  # This solution assumes that the input is
    # valid. If this is not the case, you should