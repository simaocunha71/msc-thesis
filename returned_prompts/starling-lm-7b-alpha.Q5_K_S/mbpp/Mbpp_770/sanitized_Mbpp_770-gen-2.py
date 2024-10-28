def odd_num_sum(n):
    sum_of_fourth_power = 0
    for i in range(1, 2 * n + 1, 2):
        sum_of_fourth_power += i ** 4
    return sum_of_fourth_power