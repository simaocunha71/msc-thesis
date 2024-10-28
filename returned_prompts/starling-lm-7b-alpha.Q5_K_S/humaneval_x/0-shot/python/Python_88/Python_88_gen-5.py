# Solution 1
def sort_array(array):
    first = array[0] + array[-1]
    if first % 2 == 0:
        array.sort(reverse=True)
    else:
        array.sort(reverse=False)
    return array

# Solution 2
def sort_array(array):
    if sum(array[:1]) % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array, reverse=False)

# Solution 3
def sort_array(array):
    if sum(array[:1]) % 2 == 0:
        array.sort(reverse=True)
    else:
        array.sort(reverse=False)
    return array

# Solution 4
def sort_array(array):
    return sorted(array, reverse=(sum(array[:1]) % 2 == 0))

# Solution 5
def sort_array(array):
    if sum(array[:1]) % 2 == 0:
        array = array[::-1]
    return sorted(array)

# Solution 6
def sort_array(array):
    return sorted(array, reverse=sum(array[:1]) % 2 == 0)

# Solution 7
def sort_array(array):
    return [sorted(array)[::-1] if sum(array[:1]) % 2 == 0 else sorted(array)][0]

# Solution 8
def sort_array(array):
    array[:] = sorted(array)
    array[:1] = array[:1][::-1] if sum(array[:1]) % 2 == 0 else array[:1]
    return array

# Solution 9
def sort_array(array):
    array[:] = sorted(array)
    array[:1] = array[:1][::-1] if array[:1].pop(0) % 2 == 0 else array[:1]
    return array

# Solution 10
def sort_array(array):
    array[:] = sorted(array)
    array[:1] = array[:1][::-1] if array[: