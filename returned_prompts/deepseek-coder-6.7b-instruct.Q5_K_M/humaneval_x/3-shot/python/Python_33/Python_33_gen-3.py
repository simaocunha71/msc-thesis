    divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    divisible_by_three.sort()

    for i in range(len(l)):
        if i % 3 == 0:
            l[i] = divisible_by_three[i // 3]

    return l


