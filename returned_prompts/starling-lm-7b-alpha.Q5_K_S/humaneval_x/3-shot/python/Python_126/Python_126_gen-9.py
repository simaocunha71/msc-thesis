    for i in range(len(lst)-1):
        if lst[i+1] < lst[i]:
            return False
    return True


