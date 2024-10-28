def start_withp(my_list):
    result = []
    for i in my_list:
        if i[0] == 'p':
            result.append(i.split()[0])
            result.append(i.split()[1])
    return tuple(result)


# 3
