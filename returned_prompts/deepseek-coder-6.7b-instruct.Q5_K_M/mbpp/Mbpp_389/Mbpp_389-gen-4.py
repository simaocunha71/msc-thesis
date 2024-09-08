def find_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        lucas = [2, 1]
        for i in range(2, n + 1):
            lucas.append(lucas[i - 1] + lucas[i - 2])
        return lucas[n]


print(find_lucas(9))  # 76


