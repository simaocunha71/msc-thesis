def pancake_sort(lst):
    def flip(i):
        lst[:i+1] = lst[:i+1][::-1]
    for i in range(len(lst)):
        # Find the maximum element in the unsorted part of the list
        max_index = lst.index(max(lst[:len(lst)-i]))
        # Flip the maximum element to the beginning of the unsorted part
        flip(max_index)
        # Flip the maximum element to its correct position
        flip(len(lst)-i-1)
    return lst