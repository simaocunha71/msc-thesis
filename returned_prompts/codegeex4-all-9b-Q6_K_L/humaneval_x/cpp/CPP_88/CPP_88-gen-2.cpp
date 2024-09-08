def sort_array(array):
    if len(array) <= 1:
        return array
    if (array[0] + array[-1]) % 2 == 0:
        array.sort(reverse=True)
    else:
        array.sort()
    return array

B:
def sort_array(array):
    if len(array) <= 1:
        return array
    if (array[0] + array[-1]) % 2 == 0:
        array.sort()
    else:
        array.sort(reverse=True)
    return array

C:
def sort_array(array):
    if len(array) <= 1:
        return array
    if (array[0] + array[-1]) % 2 != 0:
        array.sort(reverse=True)
    else:
        array.sort()
    return array

D:
def sort_array(array):
    if len(array) <= 1:
        return array
    if (array[0] + array[-1]) % 2 == 0:
        array.sort()
    else:
        array.sort(reverse=False)
    return array

E:
def sort_array(array):
    if len(array) <= 1:
        return array
    if (array[0] + array[-1]) % 2 != 0:
        array.sort()
    else:
        array.sort(reverse=True)
    return array

F:
def sort_array(array):
    if len(array) <= 1:
        return array
    if (array[0] + array[-1]) % 2 == 0:
        array.sort(reverse=False)
    else:
        array.sort()
    return array

G:
def sort_array(array):
    if len(array) <= 1:
        return array
    if (array[0] + array[-1]) % 2 == 0:
        array.sort(reverse=False)
    else:
        array.sort(reverse=True)
    return array

H:
def sort_array(array):
    if len(array) <= 1:
        return array
    if (array[0] + array[-1]) % 2 == 0:
        array.sort(reverse=False)
    else:
        array.sort(reverse=True)
    return array

I:
def sort_array(array):
    if len(array) <= 1:
        return array
    if (array[0] + array[-1]) % 2 == 0:
        array.sort(reverse=True)
    else:
        array.sort(reverse=False)
    return array

J:
def sort