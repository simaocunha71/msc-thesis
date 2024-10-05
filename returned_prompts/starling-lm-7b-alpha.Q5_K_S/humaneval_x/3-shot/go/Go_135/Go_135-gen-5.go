    result := 0
    for i := 0; i < len(arr); i++ {
        if i == 0 {
            result = i
        }else if arr[i] > arr[i - 1] {
            result = i
        }
    }
    if result == len(arr) - 1 {
        return -1
    }
    return result
}



