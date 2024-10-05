    for i := len(arr) - 1; i > 0; i-- {
        if arr[i] < arr[i-1] {
            if i == 1 {
                return false
            }
            arr[i], arr[i-1] = arr[i-1], arr[i]
            goto A
        }
    }
    return true
}
