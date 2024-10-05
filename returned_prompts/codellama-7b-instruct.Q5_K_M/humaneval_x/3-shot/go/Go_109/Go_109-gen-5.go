    if len(arr) == 0{
        return true
    }

    sorted := make([]int, len(arr))
    copy(sorted, arr)
    sort.Ints(sorted)

    for i:=0; i<len(arr); i++{
        if sorted[i]!=arr[i]{
            return true
        }
    }
    return false
}



