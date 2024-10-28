
def exchange(lst1, lst2):
    lst2_len = len(lst2)
    lst1_len = len(lst1)
    if lst1_len == 0:
        return "NO"
    if lst2_len == 0:
        return "NO"

    # if the first element of lst1 is even, then return "YES"
    if lst1[0] % 2 == 0:
        return "YES"

    # if the first element of lst2 is even, then exchange the first element of lst1 with it.
    # and then check if the first element of lst1 is even.
    if lst2[0] % 2 == 0:
        lst1[0], lst2[0] = lst2[0], lst1[0]
        return exchange(lst1, lst2)

    # if the first element of lst2 is odd, then we need to find an odd element from lst1.
    # if we find one, then exchange it with the first element of lst2.
    # and then check if the first element of lst1 is even.
    for i in range(1, lst1_len):
        if lst1[i] % 2 == 1:
            lst1[0], lst1[i] = lst1[i], lst1[0]
            return exchange(lst1, lst2)

    # if we couldn't find an odd element from lst1, then return "NO"
    return "NO"
