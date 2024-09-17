
def binary_search(lst, left, right, x):
    if right >= left:
        mid = (left + right) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            return binary_search(lst, left, mid - 1, x)
        else:
            return binary_search(lst, mid + 1, right, x)
    else:
        return -1


