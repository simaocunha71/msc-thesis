def search(array):
    for i in range(0,len(array)-1):
        if array[i]!=array[i+1]:
            return array[i+1]
    return array[-1]