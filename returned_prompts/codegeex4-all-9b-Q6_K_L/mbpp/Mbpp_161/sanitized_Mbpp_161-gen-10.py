def remove_elements(main_list, to_remove):
    for element in to_remove:
        if element in main_list:
            main_list.remove(element)
    return main_list