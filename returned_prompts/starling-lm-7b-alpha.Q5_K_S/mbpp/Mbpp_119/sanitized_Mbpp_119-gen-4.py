import unittest
def search(arr):
    x = arr[-1]
    while arr:
        if x == arr[-1]:
            arr.pop()
        else:
            break
    return arr[0]