    sorted_copy := make([]int,len(arr))
    copy(sorted_copy, arr)
    sort.Ints(sorted_copy)

    for i, e := range arr {
        if sorted_copy[i] != e {
            return false
        }
    }
    return true
}



