def sort_array(arr):
    s = sum(arr)
    return sorted(arr, reverse=s%2==0)

B:
def sort_array(arr):
    s = sum(arr)
    return sorted(arr, reverse=s%2==0) if len(arr) > 1 else arr

C:
def sort_array(arr):
    if len(arr) <= 1:
        return arr
    else:
        s = sum(arr)
        if s % 2 == 0:
            return sorted(arr, reverse=True)
        else:
            return sorted(arr)

D:
def sort_array(arr):
    if len(arr) == 0:
        return arr
    else:
        s = sum(arr)
        return sorted(arr, reverse=s%2==0)

E:
def sort_array(arr):
    if len(arr) == 0:
        return arr
    else:
        s = sum(arr)
        return sorted(arr, reverse=s%2==0)

F:
def sort_array(arr):
    if len(arr) == 0:
        return arr
    else:
        s = sum(arr)
        return sorted(arr, reverse=s%2==0)

G:
def sort_array(arr):
    if len(arr) <= 1:
        return arr
    else:
        s = sum(arr)
        return sorted(arr, reverse=s%2==0)

H:
def sort_array(arr):
    if len(arr) == 1:
        return arr
    else:
        s = sum(arr)
        return sorted(arr, reverse=s%2==0)

I:
def sort_array(arr):
    if len(arr) == 1:
        return arr
    else:
        s = sum(arr)
        return sorted(arr, reverse=s%2==0)

J:
def sort_array(arr):
    if len(arr) > 1:
        s = sum(arr)
        return sorted(arr, reverse=s%2==0)
    else:
        return arr

K:
def sort_array(arr):
    if len(arr) > 1:
        s = sum(arr)
        if s % 2 == 0:
            return sorted(arr, reverse=True)
        else:
            return sorted(arr)
    else:
        return arr

L:
def sort_array(arr):
    if len(arr) > 1:
        s = sum(arr)
        if s % 2 == 0:
            return sorted(arr, reverse=True)
        else:
            return sorted(arr)
    else:
        return arr

M:
