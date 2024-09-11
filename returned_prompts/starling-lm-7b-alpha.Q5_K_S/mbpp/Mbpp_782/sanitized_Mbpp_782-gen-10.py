def odd_length_sum(arr):
    # Initialize sum to 0
    sum = 0
    # Iterate over all subarrays of odd length
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            sum += sum(arr[i:j+1]) if len(arr[i:j+1])%2 == 1 else 0
    return sum