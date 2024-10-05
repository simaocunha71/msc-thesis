    # Time Complexity = O(n)
    # Space Complexity = O(1)

    # Greater than 0
    # Greater than or equal to the value of the integer itself
    # Frequency greater than or equal to the value of the integer itself
    # if the number of frequency greater than or equal to itself

    # 1. Sort the list
    lst.sort()
    # 2. Find the first number greater than zero
    for i in range(len(lst)):
        if lst[i] > 0:
            # 3. Find the first number greater than or equal to the value of the integer itself
            for j in range(i, len(lst)):
                if lst[j] >= lst[i]:
                    # 4. If the number of frequency greater than or equal to itself
                    if lst[j] == lst[j] and lst[j] >= lst[j]:
                        return lst[j]

    return -1
