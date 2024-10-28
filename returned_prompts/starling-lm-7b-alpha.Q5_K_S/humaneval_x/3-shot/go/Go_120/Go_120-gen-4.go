    sort.Ints(arr)
    n := len(arr)
    if k > n {
        return arr
    }
    return arr[n-k:]
}



