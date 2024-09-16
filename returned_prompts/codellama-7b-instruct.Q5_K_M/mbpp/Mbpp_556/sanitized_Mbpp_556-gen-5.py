def find_Odd_Pair(arr, k):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i]^arr[j]) == k:
                count += 1
    return count