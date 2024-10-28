    for i := 0; i < len(arr); i++ {
        if i > 0 && arr[i] <= arr[i-1] {
            return i
        }
    }
    return -1
}



