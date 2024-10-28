    for idx, num in enumerate(l):
        for num2 in l[idx + 1:]:
            if num + num2 == 0:
                return True
    return False


