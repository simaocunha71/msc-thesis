    open_count = 0
    close_count = 0

    for char in lst[0]:
        if char == '(':
            open_count += 1
        elif char == ')':
            open_count -= 1

    if open_count != 0:
        return 'No'

    open_count = 0
    for char in lst[1]:
        if char == '(':
            open_count += 1
        elif char == ')':
            open_count -= 1

        if open_count < 0:
            return 'No'

    return 'Yes' if open_count == 0 else 'No'  # if there are open parentheses left, it's not possible to make a good string


