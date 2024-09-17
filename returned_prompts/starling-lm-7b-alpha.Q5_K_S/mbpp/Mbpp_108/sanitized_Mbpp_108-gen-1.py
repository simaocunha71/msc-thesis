from operator import itemgetter
def merge_sorted_list(list1, list2, list3):
    sorted_list = sorted(list1 + list2 + list3)
    return sorted_list