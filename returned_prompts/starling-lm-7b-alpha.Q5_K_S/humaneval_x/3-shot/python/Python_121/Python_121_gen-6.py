    sum_odd_positions = 0
    for idx, elem in enumerate(lst):
        if idx % 2 == 0 and elem % 2 != 0:
            sum_odd_positions += elem
    return sum_odd_positions


