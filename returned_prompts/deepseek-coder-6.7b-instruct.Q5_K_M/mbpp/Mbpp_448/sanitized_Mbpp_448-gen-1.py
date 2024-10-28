def cal_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        perrin_numbers = [0, 1, 1]
        for i in range(3, n+1):
            perrin_numbers.append(perrin_numbers[i-2] + perrin_numbers[i-3])
        return sum(perrin_numbers)