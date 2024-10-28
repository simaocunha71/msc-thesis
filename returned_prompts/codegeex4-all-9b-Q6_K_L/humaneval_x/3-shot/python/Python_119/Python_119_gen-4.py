    count = 0

    for i in lst[0]:
        if i == '(':
            count += 1
        else:
            count -= 1

    for i in lst[1]:
        if i == '(':
            count += 1
        else:
            count -= 1

    if count == 0:
        return 'Yes'
    else:
        return 'No'

