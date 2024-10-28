def check_greater(arr, num):
    if num > arr[0]:
        return True
    elif num == arr[0]:
        return False
    else:
        for i in range(1, len(arr)):
            if num > arr[i]:
                return True
        return False