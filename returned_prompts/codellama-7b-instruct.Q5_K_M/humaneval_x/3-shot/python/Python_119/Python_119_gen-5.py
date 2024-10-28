    open_par = 0
    for i in lst:
        if i == '(':
            open_par += 1
        else:
            open_par -= 1

    if open_par == 0:
        return 'Yes'
    else:
        return 'No'


