    for i := 1; i < len(arr); i++ {
        if arr[i-1] > arr[i] {
            return i - 1
        }
    }
    return -1
}



