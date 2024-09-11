"""
def right_insertion(arr, value):
    for i in range(len(arr)):
        if value<arr[i]:
            return i
    return len(arr)

print(right_insertion([1,2,4,5],6))
"""

