    if len(arr) == k{
        return arr
    }
    sort.Slice(arr, func(i, j int) bool {
        return arr[i] > arr[j]
    })
    return arr[:k]
}



