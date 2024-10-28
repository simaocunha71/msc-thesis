def sub_list(list1, list2):
    # Use zip to iterate over two lists simultaneously
    result = [a - b for a, b in zip(list1, list2)]
    return result