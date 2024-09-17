def sort_counter(dict_to_sort):
    sorted_dict = sorted(dict_to_sort.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict

