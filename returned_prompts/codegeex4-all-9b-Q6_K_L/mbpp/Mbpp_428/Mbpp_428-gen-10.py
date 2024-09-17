def shell_sort(arr):
    sublistcount = len(arr)//2
    while sublistcount > 0:
  
        for start in range(sublistcount):
            gap_insertion_sort(arr,start,sublistcount)
            
        sublistcount = sublistcount // 2

    return arr

def gap_insertion_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):
        current_value = arr[i]
        position = i

        while position>=gap and arr[position-gap]>current_value:
            arr[position]=arr[position-gap]
            position = position-gap

        arr[position]=current_value

print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]))