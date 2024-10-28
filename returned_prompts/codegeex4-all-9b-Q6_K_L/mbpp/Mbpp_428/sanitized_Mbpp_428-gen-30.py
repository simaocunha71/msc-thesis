def shell_sort(arr):
    sublistcount = len(arr)//2
    while sublistcount > 0:
  
        for start in range(sublistcount):
            gap_insertion_sort(arr,start,sublistcount)
            
        sublistcount = sublistcount // 2

    return arr