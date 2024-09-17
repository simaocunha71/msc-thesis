def get_median(list1, list2, n):
    merged_list = []
    idx1 = idx2 = 0
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] < list2[idx2]:
            merged_list.append(list1[idx1])
            idx1 += 1
        else:
            merged_list.append(list2[idx2])
            idx2 += 1
    merged_list.extend(list1[idx1:] + list2[idx2:])
    n = len(merged_list)
    if n % 2 == 0:
        return (merged_list[n//2 - 1] + merged_list[n//2]) / 2
    else:
        return merged_list[n//2]