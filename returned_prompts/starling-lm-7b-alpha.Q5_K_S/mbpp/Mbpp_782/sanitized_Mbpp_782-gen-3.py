def odd_length_sum(arr):
    return sum(sum(arr[i:j+1]) for i in range(len(arr)) for j in range(i,len(arr),2))