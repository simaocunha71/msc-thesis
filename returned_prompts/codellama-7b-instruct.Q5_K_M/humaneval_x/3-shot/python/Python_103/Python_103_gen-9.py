    if n > m:
        return -1

    num_list = list(range(n, m + 1))
    avg = sum(num_list) / len(num_list)

    return bin(round(avg))[2:]


