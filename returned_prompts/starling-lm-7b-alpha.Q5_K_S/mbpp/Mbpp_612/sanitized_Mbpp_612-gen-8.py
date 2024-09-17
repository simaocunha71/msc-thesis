def merge(l):
    first_list = []
    second_list = []
    for i in l:
        first_list.append(i[0])
        second_list.append(i[1])
    return [first_list, second_list]