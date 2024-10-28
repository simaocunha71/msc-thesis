    for i := 0; i < k; i++ {
        max := arr[0]
        for j := 1; j < len(arr); j++ {
            if arr[j] > max {
                max = arr[j]
            }
        }
        arr[i] = max
        sort.Ints(arr[:i])
    }
    return arr[:k]
}


