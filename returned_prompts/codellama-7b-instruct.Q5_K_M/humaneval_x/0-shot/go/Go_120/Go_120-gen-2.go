    for i := range arr {
        for j := i + 1; j < len(arr); j++ {
            if arr[i] < arr[j] {
                arr[i], arr[j] = arr[j], arr[i]
            }
        }
    }
    sort.Ints(arr)
    return arr[:k]
}

