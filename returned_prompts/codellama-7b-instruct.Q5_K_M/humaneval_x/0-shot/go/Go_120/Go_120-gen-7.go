    for i := range arr {
        for j := i + 1; j < len(arr); j++ {
            if arr[i] < arr[j] {
                arr[i], arr[j] = arr[j], arr[i]
            }
        }
    }

    for i := 0; i < k; i++ {
        arr[i] = arr[len(arr) - k + i]
    }

    return arr
}
