def get_median(list1, list2, size):
    if len(list1) != len(list2):
        raise ValueError("Input lists must be of the same size")
    if not all(list1[i] <= list1[i+1] for i in range(len(list1)-1)) or not all(list2[i] <= list2[i+1] for i in range(len(list2)-1)):
        raise ValueError("Input lists must be sorted")
    combined = sorted(list1 + list2)
    return