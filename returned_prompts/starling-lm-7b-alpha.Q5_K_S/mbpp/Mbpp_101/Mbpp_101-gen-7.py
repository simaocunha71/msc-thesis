def kth_element(arr, k):
    return arr[k-1]

# assert kth_element([12,3,5,7,19], 2) == 3

def test_kth_element():
    assert kth_element([12,3,5,7,19], 2) == 3

test_kth_element()

"""
However, the above function will not work if the kth element does not exist in the array.
To handle this, you can modify the function to check if the array is long enough to have a kth element,
and if not, return None.
"""

def kth_element_safe(arr, k):
    if len(arr) < k:
        return None
    else:
        return arr[k-1]

def test_kth_element_safe():
    assert kth_element_safe([12,3,5,7,19], 2) == 3
    assert kth_element_safe([12,3,5,7,19], 6) == None

test_kth_element_safe()

"""
In addition, you can also modify the function to return the closest element to the kth index if the kth element does not exist in the array.
"""

def kth_element_near(arr, k):
    if len(arr) < k:
        return None
    else:
        return arr[k-1]

def test_kth_element_near():
    assert kth_element_near([12,3,5,7,19], 2) == 3
    assert kth_element_near([12,3,5,7,19], 6) == 19

test_kth_element_near()

"""
To find the kth smallest element in a list of lists, you can sort the list of lists and return the kth element in the resulting list.
"""

def kth_smallest_in_list(arr, k):
    sorted_arr = sorted(arr)
    return sorted_arr[k-1]

def test_