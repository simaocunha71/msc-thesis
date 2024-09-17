def search(test_arr):
    if len(test_arr) == 1:
        return test_arr[0]
    elif len(test_arr) == 2:
        if test_arr[0] == test_arr[1]:
            return test_arr[0]
        else:
            return test_arr[1]
    else:
        mid = int(len(test_arr)/2)
        if test_arr[mid] != test_arr[mid+1]:
            return search(test_arr[mid:mid+1])
        else:
            if test_arr[mid] != test_arr[mid-1]:
                return search(test_arr[mid-1:mid])
            else:
                return search(test_arr[mid+1:])