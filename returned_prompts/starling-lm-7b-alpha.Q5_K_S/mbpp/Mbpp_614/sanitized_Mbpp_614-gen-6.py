def cummulative_sum(tlist):
    # Initialize cummulative sum
    cummul_sum = 0

    # Iterate through the list and add each element to cummul_sum
    for t in tlist:
        for i in t:
            cummul_sum += i

    return cummul_sum