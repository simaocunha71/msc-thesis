def find_Max_Num(arr):
    arr.sort(reverse=True)
    num = ''
    for i in range(len(arr)):
        num += str(arr[i])
    return int(num)