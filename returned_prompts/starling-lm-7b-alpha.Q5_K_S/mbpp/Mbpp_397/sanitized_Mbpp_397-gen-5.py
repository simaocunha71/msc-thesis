def median_numbers(x,y,z):
    arr = [x,y,z]
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr)//2] + arr[len(arr)//2 - 1])/2
    else:
        return arr[len(arr)//2]