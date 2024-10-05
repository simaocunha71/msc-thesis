    sort.Ints(lst)
    if len(lst) < 2 {
        return nil
    }
    for i := 1; i < len(lst); i++ {
        if lst[i] > lst[0] {
            return lst[i]
        }
    }
    return nil
}