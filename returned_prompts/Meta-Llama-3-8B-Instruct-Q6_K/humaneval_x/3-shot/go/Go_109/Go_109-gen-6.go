    if len(arr) == 0 {
        return true
    }
    var sorted_arr []int
    sorted_arr = append(sorted_arr, arr[0])
    for i := 1; i < len(arr); i++ {
        if arr[i] <= sorted_arr[len(sorted_arr)-1] {
            sorted_arr = append(sorted_arr, arr[i])
        } else {
            return false
        }
    }
    return true
}