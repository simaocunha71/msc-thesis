def largest_subset(lst):
    # sort the list
    lst.sort()
    # initialize the list of sizes
    sizes = [1]*len(lst)
    # iterate through the list
    for i in range(len(lst)):
        for j in range(i):
            # if the pair is divisible
            if lst[i] % lst[j] == 0:
                # update the size of the largest subset
                sizes[i] = max(sizes[i], sizes[j] + 1)
    # return the maximum size
    return max(sizes)