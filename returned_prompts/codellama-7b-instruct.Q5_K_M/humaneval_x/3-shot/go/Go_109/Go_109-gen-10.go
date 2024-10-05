    if len(arr) == 0{
        return true
    }
    var sorted_arr = make([]int, len(arr))
    copy(sorted_arr, arr)
    sort.Ints(sorted_arr)
    for i := 0; i < len(arr); i++ {
        if sorted_arr[i] != arr[i]{
            return true
        }
    }
    return false
}



