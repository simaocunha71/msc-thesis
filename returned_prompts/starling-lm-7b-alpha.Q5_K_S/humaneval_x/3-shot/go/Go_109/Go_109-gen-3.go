    sorted := make([]int, len(arr))
    copy(sorted, arr)
    sort.Ints(sorted)

    for i, v := range arr {
        if sorted[i] != v {
            return false
        }
    }

    return true
}



