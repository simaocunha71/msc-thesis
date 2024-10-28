    hex_num = list(num)
    hex_num = [int(x) for x in hex_num if x.isdigit()] + [x for x in hex_num if x in "ABCDEF"]
    count = 0

    for i in hex_num:
        if i in [2, 3, 5, 7, 11, 13]:
            count += 1

    return count


