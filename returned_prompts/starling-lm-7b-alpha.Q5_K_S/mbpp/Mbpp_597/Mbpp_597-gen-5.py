
def find_kth(list1, list2, k):
    if k > len(list1) + len(list2):
        return None
    if k <= len(list1):
        return list1[k - 1]
    if k <= len(list1) + len(list2):
        return max(list1[k - 1], list2[k - 1 - len(list1)])


