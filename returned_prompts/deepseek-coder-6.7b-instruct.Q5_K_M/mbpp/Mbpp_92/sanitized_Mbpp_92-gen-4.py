def is_undulating(n):
    num = str(n)
    for i in range(2, len(num)):
        if num[i] == num[i-1] or num[i] != num[i-2]:
            return False
    return True