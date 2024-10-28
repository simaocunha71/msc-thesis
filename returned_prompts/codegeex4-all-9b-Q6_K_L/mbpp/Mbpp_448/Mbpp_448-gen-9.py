def cal_sum(n):
    perrin_numbers = [0, 2, 3]
    for i in range(3, n+1):
        perrin_numbers.append(perrin_numbers[i-1] + perrin_numbers[i-2])
    return sum(perrin_numbers)

