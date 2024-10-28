    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)
    if lst[0] == lst[1] {
        return nil
    }
    return lst[1]
}