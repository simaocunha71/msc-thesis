def merge(lists):
    result = [[], []]
    for sub_list in lists:
        result[0].append(sub_list[0])
        result[1].append(sub_list[1])
    return [result[0] + [sub_list[0] for sub_list in lists], result[1] + [sub_list[1] for sub_list in lists]]