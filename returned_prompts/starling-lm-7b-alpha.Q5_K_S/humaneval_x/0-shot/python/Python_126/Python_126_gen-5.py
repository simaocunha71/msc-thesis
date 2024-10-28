    # Code here

    if len(lst) == 1:
        return True
    if len(lst) == 0:
        return True
    if len(lst) == 2:
        if lst[0] == lst[1]:
            return True
        else:
            return False
    else:
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                return False
        return True



```
