    if len(arr) == 0 {
        return true
    }
    last := arr[0]
    for _, v := range arr {
        if v < last {
            return false
        }
        last = v
    }
    return true
}