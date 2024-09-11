"""
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


print(check_greater([1, 2, 3, 4, 5], 4))
"""

def check_greater(arr, num):
    return num > max(arr)

print(check_greater([1, 2, 3, 4, 5], 4))


def check_greater(arr, num):
    return num > max(arr)

print(check_greater([1, 2, 3, 4, 5], 4))






















"""
def check_greater(arr, num):
    for elem in arr:
        if elem < num:
            return True
    return False

print(check_greater([1, 2, 3, 4, 5], 4))
"""





"""
def check_greater(arr, num):
    return num > max(arr)

print(check_greater([1, 2, 3, 4, 5], 4))
"""


"""
def check_greater(arr, num):
    if num > max(arr):
        return True
    else:
        return False

print(check_greater([1, 2, 3, 4, 5], 4))
"""




"""
def check_greater(arr, num):
    if num > max(arr):
        return True
    else:
        return False

print(check_greater([1, 2, 3, 4, 5], 4))
"""




"""
def check_greater(arr, num):
    if num > max(arr):
        return True
    else:
        return False

print(check_gre