def len_log(my_list):
    longest = 0
    for word in my_list:
        if len(word) > longest:
            longest = len(word)
    return longest