    if len(arr) == 0 {
        return true
    }
    sorted := make([]int, len(arr))
    copy(sorted, arr)
    sort.Ints(sorted)
    min_index := math.MaxInt64
    for i, v := range arr {
        if v == sorted[0] {
            min_index = i
            break
        }
    }
    for i := 0; i < len(arr); i++ {
        if arr[(min_index+i)%len(arr)] != sorted[i] {
            return false
        }
    }
    return true
}

