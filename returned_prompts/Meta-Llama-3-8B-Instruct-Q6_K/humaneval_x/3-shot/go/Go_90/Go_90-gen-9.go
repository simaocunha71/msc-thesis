    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)
    if len(lst) > 2 {
        return lst[1]
    } else {
        return nil
    }
}
