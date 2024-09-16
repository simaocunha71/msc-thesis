"""
def get_median(list1, list2, length):
    # Find the middle indexes
    index1 = length // 2
    index2 = length // 2 - 1

    # Find the medians
    median1 = (list1[index1] + list1[index1 - 1]) / 2
    median2 = (list2[index2] + list2[index2 - 1]) / 2

    return (median1 + median2) / 2
"""