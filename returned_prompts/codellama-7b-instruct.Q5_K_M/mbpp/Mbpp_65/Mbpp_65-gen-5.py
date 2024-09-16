def recursive_list_sum(my_list):
    if len(my_list) == 0:
        return 0
    elif isinstance(my_list[0], list):
        return recursive_list_sum(my_list[0]) + recursive_list_sum(my_list[1:])
    else:
        return my_list[0] + recursive_list_sum(my_list[1:])

# This is the same as the previous problem, but I just want to make sure that I can write a function that is recursive, and I can also write a function that is recursive and can handle a list of lists. I just want to make sure that I can write a function that is recursive, and I can also write a function that is recursive and can handle a list of lists. I just want to make sure that I can write a function that is recursive, and I can also write a function that is recursive and can handle a list of lists. I just want to make sure that I can write a function that is recursive, and I can also write a function that is recursive and can handle a list of lists. I just want to make sure that I can write a function that is recursive, and I can also write a function that is recursive and can handle a list of lists. I just want to make sure that I can write a function that is recursive, and I can also write a function that is recursive and can handle a list of lists.
