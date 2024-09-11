def count_Occurrence(tuple_list, list_to_count):
    return sum(tuple_list.count(i) for i in list_to_count)  # or use collections.Counter(tuple_list).values()