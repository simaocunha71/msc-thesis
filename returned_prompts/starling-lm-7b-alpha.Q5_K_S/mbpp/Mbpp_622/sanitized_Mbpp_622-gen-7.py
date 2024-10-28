def get_median(list_a, list_b, size):
    merged_list = []
    for i in range(size):
        if len(list_a) == 0:
            merged_list.append(list_b.pop(0))
        elif len(list_b) == 0:
            merged_list.append(list_a.pop(0))
        elif list_a[0] <= list_b[0]:
            merged_list.append(list_a.pop(0))
        else:
            merged_list.append(list_b.pop(0))
    if len(merged_list) % 2 == 0:
        return (merged_list[len(merged_list)//2-1] + merged_list[len(merged_list)//2]) / 2.0
    else:
        return merged_list[len(merged_list)//2]