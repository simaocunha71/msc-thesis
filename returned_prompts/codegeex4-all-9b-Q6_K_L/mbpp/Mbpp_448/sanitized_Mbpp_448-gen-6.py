def cal_sum(n):
    # initialize the first two perrin numbers
    perrin = [0, 2, 3]
    # calculate the rest of the perrin numbers
    for i in range(3, n+1):
        perrin.append(perrin[i-1] + perrin[i-2] - perrin[i-3])
    # calculate the sum of the perrin numbers
    return sum(perrin)