    if len(lst) < 2 {
        return nil
    }
    sorted := make([]int,len(lst))
    copy(sorted, lst)
    sort.Ints(sorted)
    return sorted[1]
}



