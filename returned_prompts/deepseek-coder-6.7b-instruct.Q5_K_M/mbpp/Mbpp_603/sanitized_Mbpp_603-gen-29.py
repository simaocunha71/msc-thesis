def get_ludic(n):
    if n<=0:
        return []
    else:
        lucas = [2, 1]
        for i in range(2, n):
            lucas.append(lucas[i-1] + lucas[i-2])
        return lucas[:-1]