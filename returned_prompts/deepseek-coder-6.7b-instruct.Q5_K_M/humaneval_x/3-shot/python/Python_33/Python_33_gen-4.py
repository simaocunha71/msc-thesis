    divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    divisible_by_three.sort()

    for i, v in enumerate(divisible_by_three):
        l[i*3] = v

    return l


