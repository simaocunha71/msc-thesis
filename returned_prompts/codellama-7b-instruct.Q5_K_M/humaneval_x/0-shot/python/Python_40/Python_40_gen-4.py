
    # step 1: check if the length of the list is greater than 3
    if len(l) < 3:
        return False

    # step 2: sort the list
    l.sort()

    # step 3: check for the presence of -l[0]
    if -l[0] in l[1:]:
        return True

    # step 4: check for the presence of -l[-1]
    if -l[-1] in l[:-1]:
        return True

    # step 5: return False if no triples sum to zero
    return False
