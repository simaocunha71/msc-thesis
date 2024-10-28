    for i := 1; i < k; i++ {
        for j := 0; j < i; j++ {
            if arr[j] < arr[i] {
                arr[j], arr[i] = arr[i], arr[j]
                continue A
            }
        }
    }

    sort.Ints(arr[:k])
    return arr[:k]
}

