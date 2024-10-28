
def sequential_search(arr, x):
    for i in range (0, len(arr)): 
        if (arr[i] == x): 
            return (True,i)
    return (False,-1)


