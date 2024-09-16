"""
def get_Inv_Count(arr):
    if len(arr) == 1:
        return 0
    else:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        inv_count = 0
        inv_count += get_Inv_Count(left_arr)
        inv_count += get_Inv_Count(right_arr)
        inv_count += merge_sort(left_arr, right_arr)
        return inv_count

def merge_sort(left_arr, right_arr):
    left_len = len(left_arr)
    right_len = len(right_arr)
    inv_count = 0
    left_index = 0
    right_index = 0
    result = []

    while left_index < left_len and right_index < right_len:
        if left_arr[left_index] <= right_arr[right_index]:
            result.append(left_arr[left_index])
            left_index += 1
        else:
            result.append(right_arr[right_index])
            right_index += 1
            inv_count += left_len - left_index

    result.extend(left_arr[left_index:])
    result.extend(right_arr[right_index:])
    return inv_count

assert get_Inv_Count([1,20,6,4,5]) == 5
"""
