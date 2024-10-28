def odd_length_sum(arr):
    return sum([sum(arr[i:i+k]) for k in range(1,len(arr)%2+1) for i in range(len(arr)-k+1)])