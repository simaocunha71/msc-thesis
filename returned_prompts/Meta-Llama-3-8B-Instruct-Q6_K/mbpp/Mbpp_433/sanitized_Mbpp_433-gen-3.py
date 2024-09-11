def check_greater(arr, num):
    return all(num <= x for x in arr) or all(num >= x for x in arr) or num not in arr