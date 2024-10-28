def find_kth(arr1, arr2, k):
    # If one of the arrays is empty, return the kth element from the other array
    if len(arr1) == 0:
        return arr2[k-1]
    if len(arr2) == 0:
        return arr1[k-1]
    
    # If k is 1, return the smaller of the first elements of both arrays
    if k == 1:
        return min(arr1[0], arr2[0])
    
    # If the first array is shorter than k, only consider the elements in the first array
    if len(arr1) < k:
        return find_kth(arr1, arr2[len(arr1):], k-len(arr1))
    
    # If the second array is shorter than k, only consider the elements in the second array
    if len(arr2) < k:
        return find_kth(arr1[len(arr2):], arr2, k-len(arr2))
    
    # If the middle elements of both arrays are equal, return that element
    if arr1[k//2-1] == arr2[k//2-1]:
        return arr1[k//2-1]
    
    # If the middle element of the first array is smaller than the middle element of the second array, consider the right half of the first array and the left half of the second array
    if arr1[k//2-1] < arr2[k//2-1]:
        return find_kth(arr1[k//2:], arr2[:k//2], k-k//2)
    
    # If the middle element of the first array is larger than the middle element of the second array, consider the left half of the first array and the right half of the second array