    if len(arr) <= 1 {
        return true
    }
    sorted_arr := make([]int, len(arr))
    copy(sorted_arr, arr)
    sort.Ints(sorted_arr)
    min_diff := math.MaxInt64
    for i := 0; i < len(arr); i++ {
        diff := sorted_arr[i] - arr[i]
        if diff < min_diff {
            min_diff = diff
        }
    }
    for i := 0; i < len(arr); i++ {
        if arr[i]-arr[(i-1+len(arr))%len(arr)] == min_diff {
            return true
        }
    }
    return false
}

