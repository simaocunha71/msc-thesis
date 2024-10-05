    sorted_arr := make([]int, len(arr))
    copy(sorted_arr, arr)
    sort.Ints(sorted_arr)

    for i := range arr {
        if arr[(i+1)%len(arr)] < arr[i] {
            return false
        }
    }

    return true
}



