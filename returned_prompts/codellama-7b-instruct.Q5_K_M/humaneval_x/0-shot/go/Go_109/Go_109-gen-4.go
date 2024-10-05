    for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
        if arr[i] > arr[j] {
            break A
        }
    }
    if i == j {
        return true
    }

    for i := 0; i < len(arr); i++ {
        arr[i] = arr[i] >> 1
    }
    return false
}
