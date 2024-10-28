def move_zero(lst):
    # Count the number of zeros
    zero_count = lst.count(0)
    # Remove all zeros from the list
    lst = [x for x in lst if x != 0]
    # Append the number of zeros at the end of the list
    lst.extend([0]*zero_count)
    return lst