def sequential_search(arr, element):
    is_element_in_array = False
    index = -1
    for i in range(len(arr)):
        if arr[i] == element:
            is_element_in_array = True
            index = i
            break
    return is_element_in_array, index