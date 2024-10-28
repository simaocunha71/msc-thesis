def search(arr):
    '''
    Function to find the element that appears only once in a sorted array
    '''
    n = len(arr)
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            return arr[i]
    return arr[-1]