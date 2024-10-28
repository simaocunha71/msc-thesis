    if len(lst) < 2 {
        return nil
    }

    sort.Ints(lst)
    for i := 1; i < len(lst); i++ {
        if lst[i] != lst[0] {
            return lst[i]
        }
    }

    return nil
}



