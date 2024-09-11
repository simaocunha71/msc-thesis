def last(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1

# Driver code
print(last([1,2,3], 1))




















"""
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1

# Driver code
arr = [2,3,4,10,40]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print ("Element is present at index %d" %result)
else:
    print ("Element is not present in array")
"""

"""
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1

# Driver code
arr = [2,3,4,10,40]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print ("Element is present at index %d" %result)
else:
    print ("Element is not present in array")
"""

"""
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[