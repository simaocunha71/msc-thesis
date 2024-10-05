    for i := 1; i < len(arr); i++ {
        if arr[i] >= arr[i-1]{
            return i-1
        }
    }
    return -1
}



