    sortedLst := make([]int, len(lst))
    copy(sortedLst, lst)
    sort.Ints(sortedLst)
    if len(sortedLst) < 2 {
        return nil
    }
    return sortedLst[1]
}



