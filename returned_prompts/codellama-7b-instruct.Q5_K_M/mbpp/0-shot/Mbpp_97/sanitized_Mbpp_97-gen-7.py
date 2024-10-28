def frequency_lists(lists):
    return {list[i]: lists.count(list[i]) for list in lists for i in range(len(list))}