    open_count = 0
    close_count = 0

    for c in lst[0]:
        if c == '(':
            open_count += 1
        elif c == ')':
            if open_count == 0:
                return 'No'
            open_count -= 1

    for c in lst[1]:
        if c == '(':
            close_count += 1
        elif c == ')':
            if close_count == 0:
                return 'No'
            close_count -= 1

    return 'Yes' if open_count == close_count else 'No'  # Check if open_count equals close_count


