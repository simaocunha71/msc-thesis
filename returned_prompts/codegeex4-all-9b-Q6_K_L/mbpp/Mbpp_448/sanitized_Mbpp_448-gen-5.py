def cal_sum(n):
    # Calculate the perrin numbers
    perrin_numbers = [3, 0, 2]
    for i in range(3, n + 1):
        perrin_numbers.append(perrin_numbers[i - 1] + perrin_numbers[i - 2] - perrin_numbers[i - 3])

    # Calculate the sum of perrin numbers
    return sum(perrin_numbers[:n + 1])