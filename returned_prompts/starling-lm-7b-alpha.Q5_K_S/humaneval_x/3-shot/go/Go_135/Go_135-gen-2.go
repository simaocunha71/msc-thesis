    if len(arr) == 0 {
        return -1
    }
    maxIndex := 0
    for i := 1; i < len(arr); i++ {
        if arr[i] >= arr[maxIndex] {
            maxIndex = i
        }
    }
    return maxIndex
}



