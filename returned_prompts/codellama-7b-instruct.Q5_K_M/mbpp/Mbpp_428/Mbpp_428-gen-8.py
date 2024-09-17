
def shell_sort(arr):
    sublist_count = len(arr) // 2
    while sublist_count > 0:
        for start_index in range(sublist_count):
            gap_insertion_sort(arr, start_index, sublist_count)
        sublist_count = sublist_count // 2
    return arr

def gap_insertion_sort(arr, start_index, sublist_count):
    for i in range(start_index + sublist_count, len(arr), sublist_count):
        current_value = arr[i]
        position = i
        while position > start_index and arr[position - sublist_count] > current_value:
            arr[position] = arr[position - sublist_count]
            position -= sublist_count
        arr[position] = current_value


