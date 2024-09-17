def count_Pairs(arr,n):
    arr.sort()
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i] != arr[j]):
                count += 1
    return count
arr = [1,2,1]
n = len(arr)