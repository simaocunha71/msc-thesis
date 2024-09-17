def check_distinct(t):
    # Convert tuple to list to be able to sort and find duplicates
    l = sorted(list(t))
    # Check if all elements are the same
    return all(l[i] == l[i+1] for i in range(len(l)-1))