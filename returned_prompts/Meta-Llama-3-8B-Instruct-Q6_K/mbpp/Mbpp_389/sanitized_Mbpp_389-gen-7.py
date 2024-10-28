def find_lucas(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        lucas = [2, 1]
        for i in range(2, n):
            lucas.append(lucas[i-1] + lucas[i-2])
        return lucas[-1]