def check_greater(arr, num):
    if all(num > i for i in arr):
        return True
    else:
        return False