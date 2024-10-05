    sort.Slice(arr, func(i, j int) bool { return arr[i] < arr[j] })
    for i := 0; i < len(arr); i++ {
        if arr[i] != i+1 {
            return false
        }
    }
    return true
}

