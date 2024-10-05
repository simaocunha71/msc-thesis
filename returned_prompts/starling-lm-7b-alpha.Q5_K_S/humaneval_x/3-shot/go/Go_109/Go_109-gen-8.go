    sorted_arr := make([]int, len(arr))
    copy(sorted_arr, arr)
    sort.Ints(sorted_arr)

    for i, v := range arr {
        if v != sorted_arr[i] {
            return false
        }
    }
    return true
}



