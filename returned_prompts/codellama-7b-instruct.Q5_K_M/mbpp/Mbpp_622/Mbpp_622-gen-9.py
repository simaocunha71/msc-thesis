
def get_median(list1, list2, size):
    list1_sum = sum(list1)
    list2_sum = sum(list2)
    result = (list1_sum + list2_sum) / 2
    if size % 2 == 0:
        return (result + min((list1[-1] + list2[-1]) / 2, max(list1[-1], list2[-1]))) / 2
    else:
        return result


