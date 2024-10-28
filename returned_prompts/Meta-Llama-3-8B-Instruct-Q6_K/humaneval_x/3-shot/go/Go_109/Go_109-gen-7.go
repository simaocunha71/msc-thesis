    if len(arr) == 0 {
        return true
    }
    sort.Ints(arr)
    i := 0
    for i < len(arr) {
        if arr[i] > arr[(i+1)%len(arr)] {
            return false
        }
        i += 1
    }
    return true
}