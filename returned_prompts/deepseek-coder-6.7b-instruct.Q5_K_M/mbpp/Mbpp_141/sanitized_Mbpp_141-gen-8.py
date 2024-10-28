def pancake_sort(lst):
    for i in range(len(lst), 1, -1):
        # Find the index of the maximum element in the unsorted part of the list
        max_index = lst[0:i].index(max(lst[0:i]))
        # If the maximum element is not at the front, flip it to the front
        if max_index != 0:
            lst[0:max_index+1] = reversed(lst[0:max_index+1])
        # Flip the entire unsorted part to the front
        lst[0:i] = reversed(lst[0:i])
    return lst