def find_Odd_Pair(arr,num):
    c=0
    for i in range(len(arr)):
        if (num^arr[i])&1:
            c+=1
    return c