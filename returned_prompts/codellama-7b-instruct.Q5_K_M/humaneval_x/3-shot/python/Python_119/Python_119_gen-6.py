    if len(lst) > 1:
        if lst[0] == '(':
            if lst[1] == ')':
                return 'Yes'
            else:
                return 'No'
        else:
            return 'No'
    else:
        if lst[0] == '(':
            return 'No'
        else:
            return 'Yes'


