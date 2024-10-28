def get_Inv_Count(arr):
    temp_arr = [0]*len(arr)
    return merge_sort(arr,temp_arr,0,len(arr)-1)

def merge_sort(arr,temp_arr,start,end):
    inv_count = 0
    if start < end:
        mid = (start+end)//2
        inv_count += merge_sort(arr,temp_arr,start,mid)
        inv_count += merge_sort(arr,temp_arr,mid+1,end)
        inv_count += merge(arr,temp_arr,start,mid,end)
    return inv_count

def merge(arr,temp_arr,start,mid,end):
    i = start    # Starting index for left subarray
    j = mid + 1 # Starting index for right subarray
    k = start    # Starting index to be sorted
    inv_count = 0
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # There are mid-i inversions, because all elements left to i
            # in the left subarray arr[i..mid] are greater than arr[j]
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            j += 1
        k += 1
    # Copy the remaining elements of left subarray, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    # Copy the remaining elements of right subarray, if any
    while j <= end:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    # Copy the sorted subarray into Original array
    for i in range(start, end+1):
        arr[i] = temp_arr[i]
    return inv_count

