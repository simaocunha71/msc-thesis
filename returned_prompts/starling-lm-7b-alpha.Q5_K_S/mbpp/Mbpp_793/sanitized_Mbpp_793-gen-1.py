def last(array,element):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = low + high >> 1
        if array[mid] == element:
            if mid == 0:
                return mid
            if array[mid-1] == element:
                while mid < len(array)-1 and array[mid+1] == element:
                    mid += 1
                return mid
            else:
                return mid
        elif array[mid] > element:
            high = mid - 1
        else:
            low = mid + 1
    return -1