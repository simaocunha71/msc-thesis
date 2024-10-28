    if len(arr) == 0 {
        return true
    }

    var sorted_arr []int
    for i := 1; i <= len(arr); i++ {
        sorted_arr = append(sorted_arr, i)
    }

    sort.Ints(arr)
    for _, v := range arr {
        if !(sort.SearchInts(sorted_arr, v) == len(sorted_arr)) {
            return false
        }
    }

    return true
}



