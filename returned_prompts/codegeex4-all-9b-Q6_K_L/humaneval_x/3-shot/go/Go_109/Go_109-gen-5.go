    if len(arr) == 0 {
        return true
    }
    sorted_arr := make([]int, len(arr))
    copy(sorted_arr, arr)
    sort.Ints(sorted_arr)
    min_index := len(arr)
    for i, v := range arr {
        if v == sorted_arr[0] {
            min_index = i
            break
        }
    }
    for i := min_index; i < len(arr); i++ {
        if arr[i] != sorted_arr[i-min_index] {
            return false
        }
    }
    for i := 0; i < min_index; i++ {
        if arr[i] != sorted_arr[i+len(arr)-min_index] {
            return false
        }
    }
    return true
}

