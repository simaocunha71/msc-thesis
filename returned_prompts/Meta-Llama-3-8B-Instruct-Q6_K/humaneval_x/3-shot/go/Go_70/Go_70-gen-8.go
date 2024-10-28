    if len(lst) == 0 {
        return lst
    }
    sort.Slice(lst, func(i, j int) bool {
        if len(lst) == 1 {
            return false
        }
        if i == 0 {
            return lst[i] < lst[j]
        }
        if i == len(lst) - 1 {
            return lst[i] > lst[j]
        }
        return false
    })
    return lst
}