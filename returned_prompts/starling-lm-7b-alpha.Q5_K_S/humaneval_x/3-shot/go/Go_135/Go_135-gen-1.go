    max_index := 0
    for i := 1; i < len(arr); i++ {
        if arr[max_index] < arr[i] {
            max_index = i
        } else if arr[i] < arr[max_index] {
            return -1
        }
    }
    return max_index
}



