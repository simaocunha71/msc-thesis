def get_ludic(n):
    ludic_nums = [1]
    i = 2
    while True:
        if i % 2 != 0 and i % 5 != 0:
            ludic_nums.append(i)
        if max(ludic_nums) > n:
            break
        i += 1
    return ludic_nums