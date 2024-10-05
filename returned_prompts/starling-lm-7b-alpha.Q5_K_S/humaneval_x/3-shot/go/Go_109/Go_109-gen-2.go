    sorted := make([]int, len(arr))
    copy(sorted, arr)
    sort.Ints(sorted)

    for i, v := range arr {
        if v != sorted[i] {
            return false
        }
    }
    return true
}



