def get_Inv_Count(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count

print(get_Inv_Count([1,20,6,4,5]))


# Optimized solution
def get_Inv_Count_optimized(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count

print(get_Inv_Count_optimized([1,20,6,4,5]))

# Optimized solution using merge sort
def get_Inv_Count_mergeSort(arr):
    n = len(arr)
    temp_arr = [0]*n
    return _mergeSort(arr, temp_arr, 0, n-1)

def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right)//2
        inv_count += _mergeSort(arr, temp_arr, left, mid)
        inv_count += _mergeSort(arr, temp_arr, mid+1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count

def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i+1)
            k += 1
            j += 1
    while i <= mid:
        temp_arr[k] = arr[i]