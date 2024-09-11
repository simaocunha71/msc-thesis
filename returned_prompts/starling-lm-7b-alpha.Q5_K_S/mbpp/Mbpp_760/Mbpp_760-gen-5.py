"""
def unique_Element(arr):
    if arr == sorted(arr):
        return True
    else:
        return False

"""

def unique_Element(arr):
    arr = sorted(arr)
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            return False
    return True

if __name__ == '__main__':
    print(unique_Element([1,1,1]))


"""

def unique_Element(arr):
    if len(arr) == 1:
        return True
    else:
        arr = sorted(arr)
        for i in range(len(arr)-1):
            if arr[i] != arr[i+1]:
                return False
        return True

if __name__ == '__main__':
    print(unique_Element([1,1,1]))


"""

def unique_Element(arr):
    arr = list(set(arr))
    if len(arr) == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    print(unique_Element([1,1,1]))

"""

def unique_Element(arr):
    arr = sorted(arr)
    if arr == list(set(arr)):
        return True
    else:
        return False

if __name__ == '__main__':
    print(unique_Element([1,1,1]))

"""

def unique_Element(arr):
    arr = sorted(arr)
    if arr == list(set(arr)) and arr[0] == arr[1]:
        return True
    else:
        return False

if __name__ == '__main__':
    print(unique_Element([1,1,1]))

"""

def unique_Element(arr):
    arr = sorted(arr)
    if arr == list(set(arr)) and len(arr) == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    print(unique_Element([1,1,1]))
