def is_undulating(num):
    num = str(num)
    for i in range(len(num)-1):
        if num[i] != num[i+1]:
            return True
    return False