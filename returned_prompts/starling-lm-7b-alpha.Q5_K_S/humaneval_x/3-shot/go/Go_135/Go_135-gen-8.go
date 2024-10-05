    if len(arr) == 0 {
        return -1
    }
    if len(arr) == 1 {
        return 0
    }
    index := 0
    for i := 1; i < len(arr); i++ {
        if arr[i] < arr[index] {
            index = i
        }
    }
    for i := index + 1; i < len(arr); i++ {
        if arr[i] <= arr[i - 1] {
            return -1
        }
    }
    return index
}



