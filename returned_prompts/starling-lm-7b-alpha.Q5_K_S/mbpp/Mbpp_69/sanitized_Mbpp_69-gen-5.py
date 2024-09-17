def is_sublist(sublist, given_list):
    # length of sublist
    n = len(sublist)

    # traverse given_list and
    # check if all elements of
    # sublist are present in
    # given_list
    for i in range(len(given_list)):

        # If all elements of
        # sublist are present in
        # given_list
        if given_list[i:i + n] == sublist:
            return True

    return False