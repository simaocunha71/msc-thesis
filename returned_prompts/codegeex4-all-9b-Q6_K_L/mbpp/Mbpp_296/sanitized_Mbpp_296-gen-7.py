def get_Inv_Count(arr):
    # Initialize count
    count = 0
    n = len(arr)
    # Traverse array from 1 to n-1
    for i in range(1, n):
        # Traverse array from i+1 to n
        for j in range(i + 1, n):
            # If previous element is greater than current element
            if arr[i] > arr[j]:
                count += 1
    return count