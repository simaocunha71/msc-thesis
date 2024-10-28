    sorted := true
    for i := 0; i < len(arr)-1; i++ {
        if arr[i+1] < arr[i] {
            sorted = false
        }
    }
    if sorted {
        return true
    }
    for i := 0; i < len(arr); i++ {
        arr[i] = arr[i] % 2
    }
    sort.Ints(arr)
    for i := 0; i < len(arr)-1; i++ {
        if arr[i+1] < arr[i] {
            return false
        }
    }
    return true
}



