def merge(l):
    first_list = []
    second_list = []
    for sublist in l:
        first_list.append(sublist[0])
        second_list.append(sublist[1])
    return [first_list, second_list]