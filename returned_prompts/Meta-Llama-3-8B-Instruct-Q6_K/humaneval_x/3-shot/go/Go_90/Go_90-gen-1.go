    sort.Ints(lst)
    if len(lst) < 2 {
        return nil
    }
    if lst[0] == lst[1] {
        return nil
    }
    return lst[1]
}