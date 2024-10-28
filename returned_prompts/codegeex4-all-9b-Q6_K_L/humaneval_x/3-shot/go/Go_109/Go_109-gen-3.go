    if len(arr) == 0 {
        return true
    }

    sorted := make([]int, len(arr))
    copy(sorted, arr)
    sort.Ints(sorted)

    for i := 0; i < len(arr); i++ {
        if arr[i] == sorted[0] {
            return true
        }
        arr = append(arr[1:], arr[0])
    }

    return false
}



