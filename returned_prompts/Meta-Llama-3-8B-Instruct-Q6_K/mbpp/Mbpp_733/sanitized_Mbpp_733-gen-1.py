def find_first_occurrence(arr, num):
    try:
        return arr.index(num)
    except ValueError:
        return -1