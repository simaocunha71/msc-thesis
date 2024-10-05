    divisible_by_3 = [l[i] for i in range(len(l)) if i % 3 == 0]
    divisible_by_3.sort()

    for i in range(len(l)):
        if i % 3 == 0:
            l[i] = divisible_by_3[i // 3]

    return l


