"""
def right_insertion(sorted_list, value):
    insertion_point = 0
    for index, item in enumerate(sorted_list):
        if item > value:
            insertion_point = index
            break
    return insertion_point
"""
