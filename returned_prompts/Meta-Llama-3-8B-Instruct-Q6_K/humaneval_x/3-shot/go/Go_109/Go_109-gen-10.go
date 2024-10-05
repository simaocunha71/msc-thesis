    if len(arr) == 0 {
        return true
    }
    sort.Ints(arr)
    for i := 0; i < len(arr); i++ {
        if arr[i] > arr[(i+1)%len(arr)] {
            return false
        }
    }
    return true
}