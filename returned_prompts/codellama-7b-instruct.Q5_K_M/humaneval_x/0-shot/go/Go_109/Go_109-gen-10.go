    for i := range arr {
        for j := i + 1; j < len(arr); j++ {
            if arr[j] < arr[i] {
                arr[j], arr[i] = arr[i], arr[j]
                goto A
            }
        }
    }
    sort.Ints(arr)
    return true
}
