def left_insertion(sorted_list, value):
    try:
        return sorted_list.index(value)
    except ValueError:
        for i in range(len(sorted_list)):
            if sorted_list[i] > value:
                return i
        return len(sorted_list)