    if len(lst) < 2 {
        return nil
    }

    sort.Ints(lst)

    for i := 1; i < len(lst); i++ {
        if lst[i] != lst[i-1] {
            return lst[i]
        }
    }
    return nil
}

