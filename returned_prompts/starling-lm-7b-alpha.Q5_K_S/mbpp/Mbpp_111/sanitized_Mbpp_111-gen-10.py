def common_in_nested_lists(lists):
    common = []
    for list in lists:
        for item in list:
            if all(item in sublist for sublist in lists):
                common.append(item)
    return common