    if len(arr) == 0 {
        return true
    }
    if len(arr) == 1 {
        return true
    }

    sort.Ints(arr)
    for i := 0; i < len(arr) - 1; i++ {
        if arr[i] == arr[i + 1] {
            return false
        }
    }

    return true
}



