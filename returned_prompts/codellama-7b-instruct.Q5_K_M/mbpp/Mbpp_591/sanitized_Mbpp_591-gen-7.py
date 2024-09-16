def swap_List(my_List):
    first = my_List[0]
    last = my_List[-1]
    my_List[0] = last
    my_List[-1] = first
    return my_List